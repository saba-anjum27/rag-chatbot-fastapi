from fastapi import FastAPI
from .routers.file import router as _file_router
from .routers.chat import router as _chat_router

app=FastAPI()
app.include_router(_file_router)
app.include_router(_chat_router)




