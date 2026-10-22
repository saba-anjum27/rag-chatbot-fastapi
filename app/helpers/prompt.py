from langchain_core.prompts import PromptTemplate


BASE_PROMPT=PromptTemplate.from_template("You are an assistant for question answers task. you must answer the questions asked sytictly based on the provided context. " \
"if you don't know the answer, simple tell that the question is out of context. Strictly stick to the provided context" \
"Question:{question}" \
"context:{context}")