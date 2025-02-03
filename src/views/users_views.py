from typing import Dict
from src.utils.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.controllers.users_controller import UserController

users_route = APIRouter()
@users_route.post("/signup/")
def signup(body: Dict, db: Session = Depends(get_db)):
    return UserController(db).signup(body)


@users_route.post("/login/")
def login(body: Dict, db: Session = Depends(get_db)):
    return UserController(db).login(body)
