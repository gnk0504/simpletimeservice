from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Simple Time Service"}

@app.get("/time")
def get_current_time():
    now = datetime.now()
    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S")}
