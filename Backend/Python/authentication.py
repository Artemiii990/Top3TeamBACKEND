# pip install python-jose[cryptography]
# pip install passlib[bcrypt]==1.7.4
# pip install bcrypt==4.0.1

from jose import jwt, JWTError
from datetime import datetime, timedelta

from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials





SECRET_KEY = "VEryHa_rDDPa-sSWORd1234321!_!"
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