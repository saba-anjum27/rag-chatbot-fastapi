# RAG Chatbot (work in progress)

A small retrieval-augmented generation (RAG) API built for practice. Upload documents, then ask questions answered strictly from their content.

**Stack:** FastAPI · Docling (document parsing) · PGVector (Postgres vector store) · Ollama embeddings (`qwen3-embedding:0.6b`) · Google Gemini (LLM)

## Setup

1. Python 3.12+, a Postgres database with the `pgvector` extension, and [Ollama](https://ollama.com) running locally.
2. Pull the embedding model:
   ```bash
   ollama pull qwen3-embedding:0.6b
   ```
3. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your database details and Gemini API key.
5. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```
   API docs are at http://localhost:8000/docs.

## Endpoints

- `POST /file/upload?session_id=...` — upload one or more files; they are parsed, chunked and stored as embeddings.
- `POST /chat/get-chat-result?query=...` — ask a question; the answer is generated from the most relevant chunks.

## Known issues / TODO

- Chat search isn't filtered by `session_id` yet, so it searches all uploaded documents.
- Uploaded filenames and `session_id` aren't sanitized (path traversal risk) — don't deploy publicly as-is.
- Blocking calls (parsing, embedding) run inside async routes.
- Chunk size is very small (100 chars) and needs tuning.
