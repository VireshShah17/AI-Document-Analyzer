import os
from fastapi import APIRouter, UploadFile, File
from app.rag.pdf_loader import load_pdf
from app.rag.text_splitter import split_documents
from app.vectorstore.faiss_store import create_and_save_faiss_index

# Creating PDF router
router = APIRouter(prefix = "/pdf", tags = ["PDF"])

# Ensure upload directory exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok = True)

# Endpoint to upload and process PDF
@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename) # type: ignore
    # Write file to disk
    with open(file_path, "wb") as f:
        f.write(await file.read())
    # Load and split PDF
    documents = load_pdf(file_path)
    chunks = split_documents(documents)
    create_and_save_faiss_index(chunks)

    return {
        "filename": file.filename,
        "pages": len(documents),
        "chunks": len(chunks),
        "status": "Indexed successfully"
    }
