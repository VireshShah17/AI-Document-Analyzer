from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import pytesseract
from pdf2image import convert_from_path

# Windows: set tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/Lenovo/Downloads/tesseract.exe"

def load_pdf(file_path: str):
    # Try normal text extraction
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # If text exists, return it
    if any(doc.page_content.strip() for doc in documents):
        return documents

    # OCR fallback
    images = convert_from_path(file_path)
    ocr_docs = []

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        ocr_docs.append(
            Document(
                page_content=text,
                metadata={"page": i + 1}
            )
        )

    return ocr_docs