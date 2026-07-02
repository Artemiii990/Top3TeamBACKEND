from pydantic import BaseModel



class UserLogin(BaseModel):
  Username: str
  Password: str


class Token(BaseModel):
  access_token: str
  token_type: str = "bearer"