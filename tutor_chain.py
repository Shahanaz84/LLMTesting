from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner in 3 sentences"
)

llm = ChatOpenAI(model="gpt-4o-mini")
outputParser = StrOutputParser()
chain = prompt | llm | outputParser

if __name__ == "__main__":
    result = chain.invoke({"topic": "variables in python"})
    print(result)


