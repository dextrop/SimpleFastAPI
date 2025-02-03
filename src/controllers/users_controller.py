from datetime import timedelta, datetime

import jwt

from src.models import Users
from src.utils.helpers import password_hashing
from fastapi import HTTPException, status
from src.utils.constants import SECRET_KEY, ALGORITHM

class UserController():
    def __init__(self, db):
        self.db = db

    def validate_user_info(self, user_info):
        ''' Validate required user field '''
        required_fields = ["name", "email", "password"]
        validated = True
        for key in required_fields:
            if key not in user_info:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Missing {key} in request'
                )

        selected_user = self.db.query(Users).filter(Users.email == user_info["email"])
        if selected_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'User with email {user_info["email"]} already exits'
            )

        return validated

    def signup(self, user_info):
        '''
        Validate required field for user, create user
        object and add it to database ( commit )
        :param user_info: {"name": "USER_NAME", "email": "USER_EMAIL", "password": "SOMEPASS", "bio": "OPTIONAL" }
        :return:
        '''
        self.validate_user_info(user_info)
        password_hash, salt = password_hashing(password=user_info["password"])
        user_info["password"] = password_hash
        user_info["salt"] = salt
        userObj = Users(**user_info)
        self.db.add(userObj)
        self.db.commit()
        self.db.refresh(userObj)

        return {
            "status": 200,
            "message": "User created successfully",
            "payload": {
                "name": userObj.name,
                "id": userObj.id,
                "email": userObj.email,
                "bio": userObj.bio
            }
        }

    def create_access_token(self, data: dict, expires_delta: timedelta = timedelta(minutes=60)):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def login(self, login_info):
        email = login_info.get("email", None)
        password = login_info.get("password", None)

        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Missing email in request'
            )

        if not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Missing password in request'
            )

        selected_user = self.db.query(Users).filter(Users.email == email).first()
        if not selected_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'User with email {email} not found'
            )

        if not selected_user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'User is inactive'
            )

        password_hash, salt = password_hashing(
            password=login_info["password"], salt=selected_user.salt
        )

        print (selected_user.password, password_hash)
        if password_hash != selected_user.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Password mismatch'
            )

        return {
            "status": 200,
            "message": "User logged in successfully",
            "payload": {
                "token": self.create_access_token(
                    {
                        "name": selected_user.name,
                        "id": selected_user.id,
                        "email": selected_user.email,
                        "bio": selected_user.bio
                    }
                )
            }
        }
