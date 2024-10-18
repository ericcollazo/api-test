from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/finance")
def read_root():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=ZOUJ45EK95YCKCE5'
    response = requests.get(url)
    data = response.json()
    return data
