from sqlalchemy import Column, Integer, String
from sql.database import Base





class User(Base):
  __tablename__ = "Users"

  Id = Column(Integer, primary_key=True, autoincrement=True)
  Username = Column(String(100), unique=True, nullable=False)
  PasswordHash = Column(String(255), nullable=False)