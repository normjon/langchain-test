# langchain-test

Simple test of retrieval augmentation using OpenAI with OpenSearch as vector DB

## Prerequisits 

1. Valid OpenAI key
2. Docker installed on your system
3. Python3 
4. pip install openai, opensearch-py, langchain, tiktoken

## Setup

1. Set local env "OPENAI_API_KEY" to your OpenAI key value.  This will be used to make all the necessary calls to OpenAI
2. Run opensearch_start.sh located in open_search directory.  This step will start a localhost opensearch container listening on port 9600
3. Run lang_chain_retriever.py

## Results

You should be prompted to ask a question about the most recent state of the union address delivered by President Joe Biden.  Type in a question (i.e. Provide a summary on what was mentioned about taxes)
You will then be provided an output that states the question asked, the result from OpenAI and the document source
