from fastapi import APIRouter,UploadFile,File
from typing import Annotated
import shutil
import os
from pathlib import Path
from uuid import UUID
from app.config import MEDIA_PATH
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.database.connection import pgvector

router=APIRouter(prefix="/file")


@router.post("/upload")
async def upload_file( session_id:str,files:list[UploadFile]):
    media_path=Path(f'{MEDIA_PATH}/{session_id}')
    media_path.mkdir(parents=True,exist_ok=True)
    if not files:
        return {"files not found"}
    for file in files:
        file_path=Path(f'{media_path}/{file.filename}')
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

        converter=DocumentConverter()
        result=converter.convert(file_path)
        document = Document(page_content=result.document.export_to_markdown(),metadata={"source":file.filename,"session_id":session_id})
        # print("document----",document)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)

        texts=text_splitter.split_documents([document])

        pgvector.add_documents(texts)

    # return {"filenames": [file.filename for file in files]}
    return{"texts":texts}








