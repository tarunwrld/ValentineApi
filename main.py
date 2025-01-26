from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Allow requests from the frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tjwrld-be-my-valentine.static.hf.space"],  # Allow your frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

data_store = {}

class NameRequest(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/fastapi/add-names/{ticker}")
async def add_name(ticker: str, body: NameRequest):
    try:
        data_store[ticker] = body.name
        return JSONResponse(content={"added_ticker": ticker, "stored_tickers": list(data_store.values())})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fastapi/get-names")
async def get_stored_data():
    return JSONResponse(content={"stored_tickers": list(data_store.values())})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
