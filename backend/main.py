import io
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    input: str

@app.post("/Response")
async def response(body: Message):
    response = body.input.upper()*10
    print(response)
    return StreamingResponse(io.StringIO(response), media_type="text/plain")

@app.post("/MisterCommuz")
async def miserCommuz(body: Message):
    query = body.input
    try:
        storage_context = StorageContext.from_defaults(persist_dir='./storage')
        index = load_index_from_storage(storage_context)
    except:
        index = createIndex()
    
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)

    return response

def createIndex():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist()
    return index