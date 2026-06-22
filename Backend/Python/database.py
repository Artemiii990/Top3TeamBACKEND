from sqlalchemy import create_engine, MetaData



engine = create_engine("mssql+pyodbc://@localhost\\SQLEXPRESS/AppleUADB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

metadata = MetaData()