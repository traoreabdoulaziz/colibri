from fastapi import APIRouter,Body
from ..service.user import save_user
from ..model.user import User
from passlib.hash import bcrypt 

## create route
user_router = APIRouter()


## endpoint for create user
@user_router.post("/users",  tags=["Endpoint Test"], include_in_schema=False)
def create_user( user: dict = Body(...)):
    username=user['username']
    password_hash=user['password_hash']
    return save_user(username,password_hash)