import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from sqlalchemy import insert

from Backend.Python.services.authentication import hash_password

from Backend.Python.sql.database import engine
from Backend.Python.sql.tables import users





ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "AdminPassword123"



with engine.connect() as connection:
  connection.execute(
    insert(users).values(
      Username = ADMIN_USERNAME,
      PasswordHash = hash_password(ADMIN_PASSWORD),
    )
  )

  connection.commit()


print(f"Admin user '{ADMIN_USERNAME}' created")