
#!/usr/bin/env bash
set -e

APP_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="$APP_DIR/cueenv/bin/python"

if [ ! -x "$PYTHON" ]; then
    echo "CueCreator is not installed. Run install.sh first."
    exit 1
fi

exec "$PYTHON" "$APP_DIR/src/cue_creator.py" "$@"
