# AI Document Analyzer

A Python-based application for analyzing PDF documents using Retrieval Augmented Generation (RAG). This system allows users to upload PDFs, process them with LLMs, and retrieve intelligent insights through a chat interface.

## Features

- **PDF Processing**: Upload and parse PDF documents
- **Vector Store**: FAISS-based vector database for efficient semantic search
- **RAG Chain**: Retrieval Augmented Generation for context-aware responses
- **Chat API**: RESTful API for document querying and chat interactions
- **Text Splitting**: Intelligent document chunking for optimal processing

## Project Structure

```
AI-Document-Analyzer/
├── app/
│   ├── main.py              # Application entry point
│   ├── api/
│   │   ├── chat.py          # Chat API endpoints
│   │   └── pdf.py           # PDF upload and processing endpoints
│   ├── chat/
│   │   └── rag_chain.py     # RAG pipeline implementation
│   ├── core/                # Core utilities
│   ├── rag/
│   │   ├── pdf_loader.py    # PDF loading and parsing
│   │   └── text_splitter.py # Document chunking logic
│   ├── services/            # Business logic services
│   └── vectorstore/
│       └── faiss_store.py   # FAISS vector store management
├── faiss_index/             # Vector database storage
├── uploads/                 # User-uploaded PDF files
└── README.md
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Document-Analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

## Usage

### Starting the Application

```bash
python app/main.py
```

The application will start a local server with the following endpoints:

### API Endpoints

#### PDF Upload
- **POST** `/api/pdf/upload`
  - Upload a PDF document for processing
  - Body: multipart/form-data with file field
  - Response: Document metadata and processing status

#### Chat
- **POST** `/api/chat`
  - Send a query about uploaded documents
  - Body: `{"query": "Your question here"}`
  - Response: AI-generated answer with retrieved context

- **GET** `/api/chat/history`
  - Retrieve chat history
  - Response: List of previous queries and responses

## Key Components

### PDF Loader (`rag/pdf_loader.py`)
Handles PDF extraction and initial processing using PyPDF or similar libraries.

### Text Splitter (`rag/text_splitter.py`)
Splits large documents into manageable chunks with overlap for context preservation.

### FAISS Store (`vectorstore/faiss_store.py`)
Manages vector embeddings storage and similarity search operations.

### RAG Chain (`chat/rag_chain.py`)
Orchestrates the RAG pipeline: retrieval → context assembly → LLM generation.

## Configuration

Key environment variables:
- `OPENAI_API_KEY` - Your OpenAI API key
- `FAISS_INDEX_PATH` - Path to FAISS index storage
- `UPLOADS_DIR` - Directory for PDF uploads
- `CHUNK_SIZE` - Document chunk size (default: 1000)
- `OVERLAP` - Chunk overlap size (default: 100)

## Development

### Project Setup
```bash
# Install with dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

### Running Tests
```bash
pytest tests/ -v
```

## Dependencies

- **FastAPI/Flask** - Web framework
- **LangChain** - RAG orchestration
- **FAISS** - Vector similarity search
- **PyPDF** - PDF processing
- **OpenAI** - LLM API
- **Pydantic** - Data validation

See `requirements.txt` for complete list.

## Troubleshooting

### FAISS Index Issues
- Ensure `faiss_index/` directory exists and is writable
- Check that FAISS is properly installed: `pip install faiss-cpu` or `faiss-gpu`

### PDF Processing Errors
- Verify PDF is not corrupted
- Check file permissions in `uploads/` directory
- Ensure sufficient disk space for large documents

### API Connection Issues
- Verify `.env` file contains correct API keys
- Check network connectivity
- Review API rate limits

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and test thoroughly
3. Submit a pull request with description

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review error logs in the application

## Roadmap

- [ ] Multi-model support (Claude, Mistral, etc.)
- [ ] Document metadata extraction
- [ ] Advanced search filters
- [ ] User authentication
- [ ] Document versioning
- [ ] Batch processing
- [ ] Web UI dashboard
