from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

openai.api_key = 'your_openai_api_key'

app = FastAPI()

class Query(BaseModel):
    input: str

@app.post("/infer/")
async def infer(query: Query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query.input,
            max_tokens=50
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))