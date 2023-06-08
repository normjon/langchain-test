import os
import tiktoken
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

class OpenSearchVectorHelper:
    def __init__(self, opensearch_url, http_auth, use_ssl, verify_certs, ssl_assert_hostname, ssl_show_warn, index_name, embeddings):
        self.opensearch_url = opensearch_url
        self.http_auth = http_auth
        self.use_ssl = use_ssl
        self.verify_certs = verify_certs
        self.ssl_assert_hostname = ssl_assert_hostname
        self.ssl_show_warn = ssl_show_warn
        self.index_name = index_name
        self.embeddings = embeddings
        self.docsearch = None

    def loadDocsIntoIndex(self, docs):
        if self.docsearch is None:
          self.docsearch = OpenSearchVectorSearch.from_documents(
              docs,
              self.embeddings, 
              opensearch_url=self.opensearch_url, 
              http_auth=self.http_auth,     
              use_ssl = self.use_ssl,
              verify_certs = self.verify_certs,
              ssl_assert_hostname = self.ssl_assert_hostname,
              ssl_show_warn = self.ssl_show_warn,
              index_name=self.index_name)
          return self.docsearch
        else:
          self.docsearch.add_documents(docs)
          return self.docsearch

        



