import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base





SERVER_URL = os.getenv("DB_SERVER_URL")
DB_NAME = "UserDB"


master_engine = create_engine(SERVER_URL, isolation_level="AUTOCOMMIT")

with master_engine.connect() as connection:
  connection.execute(text(
    f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{DB_NAME}') "
    f"CREATE DATABASE {DB_NAME}"
  ))


engine = create_engine(SERVER_URL.replace("/master", f"/{DB_NAME}"))

Base = declarative_base()