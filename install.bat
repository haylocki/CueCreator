@echo off
setlocal

cd /d "%~dp0"

echo.
echo === CueCreator Windows Installer ===
echo.

if not exist "pyproject.toml" (
    echo Error: pyproject.toml was not found.
    pause
    exit /b 1
)

if not exist "src\cue_creator.py" (
    echo Error: CueCreator source files were not found.
    pause
    exit /b 1
)

REM Check for Python 3.11 or later.
py -3.11 --version >nul 2>&1
if errorlevel 1 (
    echo Python 3.11 was not found.
    echo.

    where winget >nul 2>&1
    if errorlevel 1 (
        echo Please install Python 3.11 or later from:
        echo https://www.python.org/downloads/windows/
        echo Then run this installer again.
        pause
        exit /b 1
    )

    echo Installing Python 3.11...
    winget install --id Python.Python.3.11 --exact ^
        --scope user --silent ^
        --accept-package-agreements ^
        --accept-source-agreements

    if errorlevel 1 (
        echo Python installation failed.
        pause
        exit /b 1
    )

    echo.
    echo Python has been installed.
    echo Close this window and run install.bat again.
    pause
    exit /b 0
)

echo Creating Python virtual environment...

if not exist "cueenv\Scripts\python.exe" (
    py -3.11 -m venv cueenv
    if errorlevel 1 (
        echo Failed to create the virtual environment.
        pause
        exit /b 1
    )
)

echo.
echo Installing CueCreator dependencies...

"cueenv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

"cueenv\Scripts\python.exe" -m pip install PyQt6 mutagen
if errorlevel 1 (
    echo Failed to install CueCreator dependencies.
    pause
    exit /b 1
)

echo.
echo Creating launcher...

(
    echo @echo off
    echo cd /d "%%~dp0"
    echo "%%~dp0cueenv\Scripts\python.exe" "%%~dp0src\cue_creator.py" %%*
) > run-cuecreator.bat

echo.
echo Installation completed successfully.
echo Run run-cuecreator.bat to start CueCreator.
pause

