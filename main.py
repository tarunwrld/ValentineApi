from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

data_store = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fastapi/add-names/{ticker}")
async def add_name(ticker: str):
    try:
        data_store[ticker] = ticker
        return {"message": "Ticker added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fastapi/get-names")
async def get_stored_data():
    return JSONResponse(content={"stored_tickers": list(data_store.values())})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
