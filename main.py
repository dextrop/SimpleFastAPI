from typing import Dict

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from controller import BooksController
from db import get_db

app = FastAPI()

@app.get("/heath_api")
def get_server_heath():
    return {"status": "Server up and running"}

def run_server():
    uvicorn.run("main:app")

@app.post("/books/")
def add_books_api(body: Dict, db: Session = Depends(get_db)):
    return BooksController(db).add_book(body)

@app.get("/books/")
def get_books_api(db: Session = Depends(get_db)):
    return BooksController(db).get_all_books()

if __name__ == '__main__':
    run_server()
