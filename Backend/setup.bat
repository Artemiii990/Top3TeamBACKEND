@echo off
setlocal
chcp 65001 > nul

set SERVER=test.c7gie2ikwu4m.eu-north-1.rds.amazonaws.com,1433
set USERNAME=admin
set PASSWORD=Master98766789

set BACKEND=%~dp0


echo ==================================================
echo                 AppleUADB ^| Setup
echo ==================================================
echo.


echo [1/5] Creating database...
sqlcmd -S %SERVER% -U %USERNAME% -P %PASSWORD% -C -i "%BACKEND%SQL\SQLQueries\CreateDatabase.sql"
if errorlevel 1 (
    echo [ERROR] Failed to create database
    pause & exit /b 1
)
echo.


echo [2/5] Creating Products table...
sqlcmd -S %SERVER% -U %USERNAME% -P %PASSWORD% -C -i "%BACKEND%SQL\SQLQueries\CreateProductsTable.sql"
if errorlevel 1 (
    echo [ERROR] Failed to create Products table
    pause & exit /b 1
)
echo.


echo [3/5] Creating Users table...
sqlcmd -S %SERVER% -U %USERNAME% -P %PASSWORD% -C -i "%BACKEND%SQL\SQLQueries\CreateUsersTable.sql"
if errorlevel 1 (
    echo [ERROR] Failed to create Users table
    pause & exit /b 1
)
echo.


echo [4/5] Seeding products...
python "%BACKEND%SQL\insert_data.py"
if errorlevel 1 (
    echo [ERROR] Failed to insert product data
    pause & exit /b 1
)
echo.


echo [5/5] Creating admin user...
python "%BACKEND%Python\scripts\create_admin.py"
if errorlevel 1 (
    echo [ERROR] Failed to create admin user
    pause & exit /b 1
)
echo.


echo ==================================================
echo                 Setup complete!
echo ==================================================
pause