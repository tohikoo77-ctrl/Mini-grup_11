#!/bin/bash
set -e

# Load environment variables manually
ENV_FILE="/usr/src/app/.env"
if [ -f "$ENV_FILE" ]; then
  echo "🔑 Loading environment variables from $ENV_FILE"
  export $(grep -v '^#' "$ENV_FILE" | xargs)
else
  echo "⚠️  No .env file found at $ENV_FILE"
fi

echo "✅ Django is ready."
echo ""
echo "========== Starting Tunnels =========="

if [ -n "$JPRQ_AUTH_KEY" ]; then
  echo "Authenticating jprq..."
  jprq auth "$JPRQ_AUTH_KEY"
  echo "Starting jprq tunnel on port 1034..."
  jprq http 1034 -s "$JPRQ_URL" > jprq.log 2>&1 &
  sleep 2
  JPRQ_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.jprq\.site' jprq.log | head -n1)
fi

echo ""
echo "========== Public URLs =========="
[ -n "$JPRQ_URL" ] && echo "🌀 jprq  → $JPRQ_URL"
echo "================================="

echo "🚀 Starting Uvicorn ASGI server with reload..."
exec uvicorn core.asgi:application \
    --host 0.0.0.0 \
    --port 1034 \
    --reload \
    --reload-dir /usr/src/app