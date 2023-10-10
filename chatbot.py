# gen ai chatbot
import os
import sys

import api
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = api.APIKEY

query = sys.argv[1]
print(query)

loader = TextLoader("./data/data.txt")
index = ''
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
