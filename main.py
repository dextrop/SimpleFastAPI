import uvicorn
from fastapi import FastAPI, Request, Depends

from src.utils.auth import JWTAuthenticationMiddleware
from src.utils.db import get_db, SessionLocal
from src.views import books_route, users_route

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = await call_next(request)
    return response

# Add the JWT Authentication Middleware
app.add_middleware(JWTAuthenticationMiddleware, dbsession=SessionLocal)

app.include_router(books_route)
app.include_router(users_route)

@app.get("/heath_api")
def get_server_heath():
    return {"status": "Server up and running"}

@app.get("/heath_api")
def get_server_heath():
    return {"status": "Server up and running"}

def run_server():
    uvicorn.run("main:app")

if __name__ == '__main__':
    run_server()
