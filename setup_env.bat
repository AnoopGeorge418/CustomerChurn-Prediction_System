@echo off
setlocal

:: Define environment paths
set "ENV_FOLDER=env"
set "ENV1=%ENV_FOLDER%\datahub_env"
set "ENV2=%ENV_FOLDER%\backend_env"

:: Ensure env folder exists
if not exist %ENV_FOLDER% mkdir %ENV_FOLDER%

:: List of environments to create
for %%E in ("%ENV1%" "%ENV2%") do (
    if exist %%E (
        echo ✅ Conda environment %%E already exists. Skipping...
    ) else (
        echo 🔹 Creating Conda environment: %%E...
        call conda env create -p %%E -f environment.yml -y
        if %ERRORLEVEL% neq 0 (
            echo ❌ Failed to create environment %%E.
            exit /b 1
        )
    )
)

echo 🎉 Both Environments Created Successfully!
echo 👉 To activate DataHub Environment: conda activate %ENV1%
echo 👉 To activate Backend Environment: conda activate %ENV2%
echo Setup completed! Happy Coding...

pause
