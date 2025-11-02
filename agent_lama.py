from langchain_ollama import OllamaLLM
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.base import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

# Local model (no API key needed)
llm = OllamaLLM(model="llama3")

db = SQLDatabase.from_uri("postgresql+psycopg2://admin:admin123@localhost:5432/employees")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

print("\n LangChain Employee Agent Ready (Ollama mode)!\n")

while True:
    question = input("Ask your question (or 'exit'): ")
    if question.lower() == "exit":
        break
    try:
        answer = agent.invoke(question)
        print("\n Answer:\n", answer, "\n")
    except Exception as e:
        print("Error:", e)
