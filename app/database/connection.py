from app.config import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER
from langchain_postgres.vectorstores import PGVector
from langchain_ollama import OllamaEmbeddings

print("db_port---",DB_PORT)

connection = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
collection_name="chatbot"

embeddings = OllamaEmbeddings(model="qwen3-embedding:0.6b")


pgvector = PGVector(embeddings=embeddings,collection_name=collection_name,connection=connection)
