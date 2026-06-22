from sqlalchemy import Table
from sql.database import engine, metadata



users = Table(
  "Users",
  metadata,
  autoload_with=engine
)

products = Table(
  "Products",
  metadata,
  autoload_with=engine
)