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
echo Creating Start Menu shortcut...

set "CUECREATOR_DIR=%~dp0"
set "CUECREATOR_LAUNCHER=%~dp0run-cuecreator.bat"
set "CUECREATOR_ICON=%~dp0cue_creator.ico"
set "START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs"

if not exist "%CUECREATOR_ICON%" (
    echo Warning: cue_creator.ico was not found.
    echo The shortcut will use the default Windows icon.
)

if not exist "%START_MENU%" mkdir "%START_MENU%"

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
    "$shell = New-Object -ComObject WScript.Shell; " ^
    "$shortcut = $shell.CreateShortcut([IO.Path]::Combine($env:APPDATA, 'Microsoft\Windows\Start Menu\Programs\CueCreator.lnk')); " ^
    "$shortcut.TargetPath = $env:CUECREATOR_LAUNCHER; " ^
    "$shortcut.WorkingDirectory = $env:CUECREATOR_DIR; " ^
    "if (Test-Path $env:CUECREATOR_ICON) { $shortcut.IconLocation = $env:CUECREATOR_ICON + ',0' }; " ^
    "$shortcut.Save()"

if errorlevel 1 (
    echo Warning: Could not create the Start Menu shortcut.
) else (
    echo Start Menu shortcut created.
)

echo.
echo Installation completed successfully.
echo You can now launch CueCreator from the Windows Start Menu.
echo You can also run run-cuecreator.bat from this folder.
pause

