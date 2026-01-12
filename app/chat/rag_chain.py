from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from app.vectorstore.faiss_store import load_faiss_index

def get_rag_chain():
    vectorstore = load_faiss_index()
    retriever = vectorstore.as_retriever(search_kwargs = {"k": 4})

    llm = OllamaLLM(
        model = "phi3:mini",
        temperature = 0.2
    )

    prompt = PromptTemplate(
        input_variables = ["context", "question"],
        template = """
            You are an assistant answering questions from the provided document context only.
            If the answer is not in the context, say "I don't know".
            Context:
            {context}

            Question:
            {question}

            Answer:
        """.strip()
    )

    return retriever, llm, prompt
