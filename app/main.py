from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from FastAPI deployed on AWS Lambda with API Gateway!"}
