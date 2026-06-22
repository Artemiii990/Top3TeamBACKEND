IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'AppleUADB')
BEGIN
    CREATE DATABASE AppleUADB;
    PRINT 'Database created';
END
ELSE
    PRINT 'Database already exists';