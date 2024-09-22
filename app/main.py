from fastapi import FastAPI
from configs.setting import test_text

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": test_text}
