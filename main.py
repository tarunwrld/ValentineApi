from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow CORS for all domains (you can restrict it to specific domains if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains to make requests (change to specific domains for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

data_store = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fastapi/add_names/{ticker}")
async def add_name(ticker: str):
    try:
        data_store[ticker] = ticker
        json_data = [{"ticker": ticker} for ticker in data_store.values()]
        return JSONResponse(content=json_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fastapi/get-names")
async def get_stored_data():
    return JSONResponse(content={"stored_tickers": list(data_store.values())})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
