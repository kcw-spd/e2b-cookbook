# in terminal run: 
# set "LANGCHAIN_TRACING_V2=true"
# set "LANGCHAIN_ENDPOINT=https://api.smith.langchain.com"
# set "LANGCHAIN_API_KEY=ls__7485b5dc6a0243f6bdf3d57ffbbc1dbf"
# set "LANGCHAIN_PROJECT=e2b-ai-github-developer-py"
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")