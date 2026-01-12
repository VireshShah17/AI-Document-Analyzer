from fastapi import APIRouter
from pydantic import BaseModel
from app.chat.rag_chain import get_rag_chain

router = APIRouter(prefix = "/chat", tags = ["chat"])


class ChatRequest(BaseModel):
    question: str


@router.post("")
def chat(request: ChatRequest):
    retriever, llm, prompt = get_rag_chain()
    docs = retriever.invoke(request.question)
    context = "\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.format(context = context, question = request.question)
    answer = llm.invoke(final_prompt)

    return {
        "question": request.question,
        "answer": answer,
        "sources": [doc.metadata for doc in docs],
    }
