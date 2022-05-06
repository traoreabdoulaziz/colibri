import json
from fastapi import FastAPI, Form
import jwt
from fastapi import Depends, HTTPException, status, Form, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .api.model.user import User
from .config.config import JWT_SECRET
from .api.routes import router
from .api.service.auth import authenticate_user
import os

## load variable environment
ENV = os.environ.get("ENV") or "local"
with open("secrets.json", "r") as f:
    secret = json.load(f)[ENV]


## create app
app = FastAPI(title="API", version="0.0.1")


### test the main page
@app.get("/", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome to API COLIBRI"}


## generate token
@app.post("/token", tags=["Authentication"])
def generate_token(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username=username, password=password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
        )
    user_obj = {
        "id": user.id,
        "username": user.username,
        "password_hash": user.password_hash,
    }
    token = jwt.encode(user_obj, JWT_SECRET)
    return {"access_token": token, "token_type": "bearer"}


## include all routes
app.include_router(router, prefix="/api")
