from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import pdf, chat
from dotenv import load_dotenv
import os

load_dotenv()

# Creating FastAPI instance
app = FastAPI(title = "AI Document Search API")

# Configuring CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500/"],  # frontend URL
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running smoothly.", "openai_key_loaded": bool(os.getenv("OPENAI_API_KEY"))}


# Including PDF router
app.include_router(pdf.router)
app.include_router(chat.router)
