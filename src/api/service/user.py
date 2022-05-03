
from fastapi import Depends, HTTPException, status
from api.model.user import User
from passlib.hash import bcrypt

## find the authenticate user
def findAuthUser(username:str,password:str):
    user=User.collection.where('username','==',username).limit(1).stream()
    if user:
        current_user=user[0]
        if bcrypt.verify(password, current_user.password_hash):
                return current_user
        else:
            return False
    else:
        return False    

## save user to Firestore        
def save_user(username,password_hash):
    user=User.collection.where('username','==',username).limit(1).stream()
    if user:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail='user already exist'
                )     
    new_user=User(username=username,password_hash=bcrypt.hash(password_hash))
    new_user.save()
    return {
        "id":new_user.id,
        "username":new_user.username,
        "password_hash":new_user.password_hash
    }
    
   