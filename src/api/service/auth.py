from email import header

from httplib2 import Authentication
from ..model.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from ...config.config import JWT_SECRET, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import Body, Depends, HTTPException, status
import jwt
from ..service.user import findAuthUser

## define the url
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# verify the authentification of the user
def authenticate_user(username: str, password: str):
    """This verify if the user is authentificate
    Args:
        username (str): username of user
        password (str): password of user
    Returns:
        user: authenticate user
    """
    user = findAuthUser(username, password)
    if user:
        return user
    else:
        return False


##get current user information
def get_current_user(token: str = Depends(oauth2_scheme)):
    """This function is used to get the current user information
    Args:
        token (str, optional): the token of user. Defaults to Depends(oauth2_scheme).
    Returns:
        user: current user
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = User.get(id=payload.get("id"))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
        )
    return user
