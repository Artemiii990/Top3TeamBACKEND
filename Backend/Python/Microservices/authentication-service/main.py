import os
from fastapi import FastAPI, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta

from passlib.context import CryptContext

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from dtos.authentication_dtos import *

from sql.database import engine, Base
from sql.model import User





app = FastAPI(title="Authentication Service")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer_scheme = HTTPBearer()



def hash_password(password: str) -> str:
  return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
  return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



def decode_token(token: str):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except JWTError:
    return None



def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> dict:
  payload = decode_token(credentials.credentials)

  if payload is None:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail = "Invalid or expired token",
      headers = {"WWW-Authenticate": "Bearer"},
    )


  return payload



@app.post("/authentication-service/login")
async def login(data: UserLogin, db: Session = Depends(get_db)):
  user = db.scalar(
    select(User).where(User.Username == data.Username)
  )


  if user is None or not verify_password(data.Password, user.PasswordHash):
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Incorrect username or password",
    )


  access_token = create_access_token({"sub": user.Username})

  return Token(access_token=access_token)



@app.post("/authentication-service/verify")
async def verify(token: Token):
  try:
    payload = jwt.decode(token.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    return {"valid": True, "username": payload["sub"]}
  except JWTError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")



@app.post("/authentication-service/users")
def get_users(db: Session = Depends(get_db)):
  return db.scalars(select(User)).all()



@app.post("/authentication-service/users/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
  user = db.scalar(select(User).where(User.Username == username))

  if not user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


  return user