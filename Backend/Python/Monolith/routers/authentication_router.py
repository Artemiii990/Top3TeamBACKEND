from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from Backend.Python.Monolith.dtos.authentication.token_response import Token
from Backend.Python.Monolith.dtos.authentication.input_dto import UserLogin

from Backend.Python.Monolith.services.authentication import verify_password, create_access_token

from Backend.Python.Monolith.sql.database import engine
from Backend.Python.Monolith.sql.tables import users





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