from fastapi import APIRouter
from app.database.connection import pgvector
from app.helpers.llm import get_llm
from app.helpers.prompt import BASE_PROMPT

router=APIRouter(prefix="/chat")

@router.post("/get-chat-result")
async def get_chat_result(query:str):
    retriever = pgvector.as_retriever(search_type="mmr",search_kwargs={'k':5,'fetch_k':10})

    results=retriever.invoke(query)
    context=""
    for i in results:
        context = context+" "+i.page_content

    llm = get_llm()
    prompt = BASE_PROMPT.format(question=query,context=context)
    answer = await llm.ainvoke(prompt)
    return answer.content[0].get("text")
