from sqlalchemy import create_engine, MetaData



engine = create_engine("mssql+pyodbc://admin:Master98766789@test.c7gie2ikwu4m.eu-north-1.rds.amazonaws.com:1433/AppleUADB?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes")

metadata = MetaData()