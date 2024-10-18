from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/finance")
def read_root():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=AXC6TASM228ZDY4O'
    response = requests.get(url)
    data = response.json()
    return data