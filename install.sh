
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/cueenv"
VENV_PYTHON="$VENV_DIR/bin/python"
LAUNCHER="$SCRIPT_DIR/run-cuecreator.sh"

cd "$SCRIPT_DIR"

echo "=== CueCreator installer ==="

if [[ ! -f pyproject.toml || ! -f src/cue_creator.py ]]; then
    echo "Error: Run this installer from the CueCreator directory."
    exit 1
fi

# Install system dependencies.
if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y python3 python3-venv

elif command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --needed python python-pip python-virtualenv

elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y python3 python3-pip python3-virtualenv

elif command -v zypper >/dev/null 2>&1; then
    sudo zypper --non-interactive install \
        python3 python3-pip python3-virtualenv

else
    echo "Error: Unsupported Linux package manager."
    exit 1
fi

# Create the virtual environment.
if command -v uv >/dev/null 2>&1; then
    echo "Creating environment with uv..."
    uv venv --python python3 "$VENV_DIR"
    INSTALLER="uv"
elif command -v virtualenv >/dev/null 2>&1; then
    echo "Creating environment with virtualenv..."
    virtualenv -p python3 "$VENV_DIR"
    INSTALLER="pip"
else
    echo "Creating environment with Python venv..."
    python3 -m venv "$VENV_DIR"
    INSTALLER="pip"
fi

# Install the application dependencies.
echo "Installing CueCreator dependencies..."

if [[ "$INSTALLER" == "uv" ]]; then
    uv pip install --python "$VENV_PYTHON" PyQt6 mutagen
else
    "$VENV_PYTHON" -m pip install --upgrade pip
    "$VENV_PYTHON" -m pip install PyQt6 mutagen
fi

# Create a permanent launcher.
cat > "$LAUNCHER" <<'LAUNCHER_EOF'
#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/cueenv/bin/python" \
    "$SCRIPT_DIR/src/cue_creator.py" "$@"
LAUNCHER_EOF

chmod +x "$LAUNCHER"

# Create an applications-menu entry for the current user.
APP_DIR="$HOME/.local/share/applications"
DESKTOP_FILE="$APP_DIR/cuecreator.desktop"
ICON_DIR="$HOME/.local/share/icons"
ICON_FILE="$ICON_DIR/cue_creator.png"

mkdir -p "$APP_DIR" "$ICON_DIR"

# Install the application icon.
if [[ -f "$SCRIPT_DIR/cue_creator.png" ]]; then
    cp "$SCRIPT_DIR/cue_creator.png" "$ICON_FILE"
else
    echo "Warning: cue_creator.png not found; using default icon."
    ICON_FILE="audio-x-generic"
fi

{
    echo "[Desktop Entry]"
    echo "Version=1.0"
    echo "Type=Application"
    echo "Name=CueCreator"
    echo "Comment=Create CUE sheets from audio files"
    printf 'Exec="%s"\n' "$LAUNCHER"
    printf 'Path=%s\n' "$SCRIPT_DIR"
    echo "Terminal=false"
    echo "Categories=AudioVideo;Audio;"
    echo "StartupNotify=true"
    printf 'Icon=%s\n' "$ICON_FILE"
} > "$DESKTOP_FILE"

# Verify the installed dependencies.
echo
echo "Checking CueCreator dependencies..."

"$VENV_PYTHON" -c '
import PyQt6
import mutagen
print("PyQt6: available")
print("mutagen: available")
'

echo
echo "Installation completed."
echo "Launch from the applications menu or run:"
echo "$LAUNCHER"
