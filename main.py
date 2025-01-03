import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/heath_api")
def get_server_heath():
    return {"status": "Server up and running"}

def run_server():
    uvicorn.run("main:app")

if __name__ == '__main__':
    run_server()
