import os
import tiktoken
from load_opensearch_docs import OpenSearchVectorHelper
from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA



# Remember to set the OPENAI_API_KEY environment variable

loader = TextLoader('./state_of_the_union.txt', encoding='utf-8')

# Prepare documents
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Define embeddings as OpenAI and LLM as OpenAI
embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0)

# Intialize OpenSearchVectorHelper and load documents into index
helper = OpenSearchVectorHelper(opensearch_url="https://localhost:9200", http_auth=("admin", "admin"), use_ssl = False, verify_certs = False, ssl_assert_hostname = False, ssl_show_warn = False, index_name="sotu", embeddings=embeddings)
docsearch = helper.loadDocsIntoIndex(docs)
retriever = docsearch.as_retriever(search_kwargs={"k":5})

#agent_prompt = PromptTemplate(
#    input_variables=['context','query'],
#    template="Use the context below to answer the following query: {query} \n\nContext: {context}\n\nAnswer:")

chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

while True:
    prompt = input("Enter your question on state of the union: ")
    print(chain(prompt))
    







