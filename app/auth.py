from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class UserRegister(BaseModel):
    username: str
    password: str


fake_users = {}


@router.post("/register")
def register(user: UserRegister):
    if user.username in fake_users:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users[user.username] = user.password

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(user: UserRegister):
    saved_password = fake_users.get(user.username)

    if not saved_password:
        raise HTTPException(status_code=404, detail="User not found")

    if saved_password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {
        "message": "Login successful"
    }