import os
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.base import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

# Not working since no credits left NEED TO ADD API KEY

db = SQLDatabase.from_uri("postgresql+psycopg2://admin:admin123@localhost:5432/employees")

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

print("\n LangChain Employee Agent Ready!\n")

while True:
    question = input("Ask your question (or 'exit'): ")
    if question.lower() == "exit":
        break
    try:
        answer = agent.invoke(question)
        print("\n Answer:\n", answer, "\n")
    except Exception as e:
        print(" Error:", e)
