from __future__ import annotations

from typing import TypedDict

from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langgraph.graph import END, START, StateGraph
from transformers import pipeline

from app.config import Settings


class GraphState(TypedDict):
    question: str
    context: list[str]
    answer: str


def build_llm() -> HuggingFacePipeline:
    settings = Settings()
    llm_pipeline = pipeline(
        "text-generation",
        model=settings.llm_model,
        tokenizer=settings.llm_model,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        device=-1,
    )
    return HuggingFacePipeline(pipeline=llm_pipeline)


def retrieve_node(state: GraphState, vector_store: FAISS) -> GraphState:
    documents = vector_store.similarity_search(state["question"], k=2)
    state["context"] = [document.page_content for document in documents]
    return state


def answer_node(state: GraphState, llm: HuggingFacePipeline) -> GraphState:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer using only the provided context. If the context does not contain the answer, say you do not know.",
            ),
            ("human", "Context:\n{context}\n\nQuestion:\n{question}"),
        ]
    )
    answer_chain = prompt | llm | StrOutputParser()
    state["answer"] = answer_chain.invoke({
        "context": "\n\n".join(state["context"]),
        "question": state["question"],
    })
    return state


def create_rag_graph(vector_store: FAISS):
    llm = build_llm()
    workflow = StateGraph(GraphState)
    workflow.add_node("retrieve", lambda state: retrieve_node(state, vector_store))
    workflow.add_node("answer", lambda state: answer_node(state, llm))
    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "answer")
    workflow.add_edge("answer", END)
    return workflow.compile()
