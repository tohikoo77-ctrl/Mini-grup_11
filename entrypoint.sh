#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py makemigrations --noinput || true
python manage.py migrate --noinput

echo "Starting service..."
exec "$@"
