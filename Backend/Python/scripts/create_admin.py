import sys, os

BACKEND = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, BACKEND)


from sqlalchemy import insert, select

from Python.services.authentication import hash_password

from Python.sql.database import engine
from Python.sql.tables import users





ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "AdminPassword123"



with engine.connect() as connection:
  exists = connection.execute(
      select(users.c.Id)
      .where(users.c.Username == ADMIN_USERNAME)
    ).first()
  
  if exists:
    print(f"User '{ADMIN_USERNAME}' already exists")
  else:
    connection.execute(
      insert(users).values(
        Username = ADMIN_USERNAME,
        PasswordHash = hash_password(ADMIN_PASSWORD),
      )
    )

    connection.commit()


    print(f"Admin user '{ADMIN_USERNAME}' created")