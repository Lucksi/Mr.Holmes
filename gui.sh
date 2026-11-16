#!/usr/bin/env bash
# Launch the Mr.Holmes web GUI from the repo root.
# Usage: ./gui.sh [port]   (default 5001)

set -e

PORT="${1:-5001}"
HOST="127.0.0.1"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GUI_DIR="$ROOT/GUI"

if ! command -v php >/dev/null 2>&1; then
  echo "[!] PHP not found. Install it with: brew install php"
  exit 1
fi

if [ ! -d "$GUI_DIR" ]; then
  echo "[!] GUI folder not found at $GUI_DIR"
  exit 1
fi

if lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "[!] Port $PORT is already in use. Try: ./gui.sh 5002"
  exit 1
fi

URL="http://$HOST:$PORT"
echo "[+] Mr.Holmes GUI on $URL  (Ctrl+C to stop)"

# Open the browser once the server is up (macOS: open, Linux: xdg-open)
( sleep 1
  if command -v open >/dev/null 2>&1; then open "$URL"
  elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$URL"
  fi ) &

cd "$GUI_DIR"
exec php -S "$HOST:$PORT"
