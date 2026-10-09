from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .prompts import SYSTEM_PROMPT,RAG_TEMPLATE

def build_answer_chain(model_name:str="gpt-4.1-mini",temperature:float=0.0):
    prompt=ChatPromptTemplate.from_messages([("system",SYSTEM_PROMPT),("human",RAG_TEMPLATE)])
    return prompt | ChatOpenAI(model=model_name,temperature=temperature)
