from typing import Dict
from src.utils.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Request, status, HTTPException
from src.controllers.books_controller import BooksController

books_route = APIRouter()
@books_route.post("/books/")
def add_books_api(body: Dict, request:Request, db: Session = Depends(get_db)):
    if not request.state.user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Your are not authorised to add book, kindly login'
        )
    return BooksController(db).add_book(body)

@books_route.get("/books/")
def get_books_api(db: Session = Depends(get_db)):
    return BooksController(db).get_all_books()
