from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
import httpx

app = FastAPI()

@app.post("/infer/")
async def infer(request: Request):
    json_body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post("http://inference_service:8000/infer/", json=json_body)
        return response.json()