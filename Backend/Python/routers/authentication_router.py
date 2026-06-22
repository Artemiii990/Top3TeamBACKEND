from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from dtos.authentication_dtos import UserLogin, Token
from authentication import verify_password, create_access_token

from database import engine
from tables import users





authentication_router = APIRouter(tags=["Authentication"])



@authentication_router.post("/authentication/login", response_model=Token)
async def login(data: UserLogin):
  with engine.connect() as connection:
    user = connection.execute(
      select(users).where(users.c.Username == data.Username)
    ).mappings().first()


  if user is None or not verify_password(data.Password, user["PasswordHash"]):
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Incorrect username or password",
    )


  access_token = create_access_token({"sub": user["Username"]})

  return Token(access_token=access_token)