from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask_llm(data: Query):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": data.query}
        ],
        model="llama-3.1-8b-instant"
    )

    return {
        "query": data.query,
        "response": response.choices[0].message.content
    }