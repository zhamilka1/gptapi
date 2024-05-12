from g4f.client import Client
from fastapi import FastAPI
from pydantic import BaseModel
import g4f.Provider.Llama

client = Client()

class Message(BaseModel):
    text:str

app = FastAPI()

@app.post("/send_message")
async def send_message(message: Message):

    response2 = client.chat.completions.create(
        model="Meta-Llama-3-70B-Instruct",
        messages=[{"role": "user", "content": message.text}],
        provider= g4f.Provider.Llama
    )
    return response2.choices[0].message.content
