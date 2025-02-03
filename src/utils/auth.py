import jwt
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from src.models import Users
from src.utils.constants import SECRET_KEY, ALGORITHM
from src.utils.db import get_db


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("email")
        if username is None:
            raise credentials_exception
        return username
    except Exception as e:
        return JSONResponse(status_code=403, content={"message": "Invalid credentials"})


class JWTAuthenticationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, bearer=HTTPBearer(), dbsession=None):
        super().__init__(app)
        self.bearer = bearer
        self.dbsession = dbsession

    async def dispatch(self, request: Request, call_next):
        authorization: HTTPAuthorizationCredentials = None
        try:
            authorization = await self.bearer(request)
        except Exception as e:
            authorization = None
            # return JSONResponse(status_code=403,
            #                     content={"message": "Credentials are required to access this resource."})

        if not authorization:
            request.state.user = None
            request.state.email = None
            response = await call_next(request)
            return response

        token = authorization.credentials
        try:
            with self.dbsession() as db:
                username = verify_token(token, HTTPException(status_code=403, detail="Invalid token or expired token"))
                user_Obj = db.query(Users).filter(
                    Users.email == username
                ).first()

                if user_Obj:
                    # Store the user in requests.state
                    request.state.user = user_Obj
                    request.state.email = user_Obj.email
                else:
                    request.state.user = None
                    request.state.email = None
        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"message": e.detail})

        response = await call_next(request)
        return response

