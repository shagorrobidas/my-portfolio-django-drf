#!/bin/bash

set -e

echo "======================================="
echo "Starting Django Application..."
echo "======================================="

# Wait for PostgreSQL
echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL started"

# Apply migrations
echo "======================================="
echo "Applying database migrations..."
echo "======================================="

python manage.py migrate --noinput

# Collect static files
echo "======================================="
echo "Collecting static files..."
echo "======================================="

python manage.py collectstatic --noinput

# Optional: Create superuser automatically
# python manage.py createsuperuser --noinput || true

echo "======================================="
echo "Starting Gunicorn Server..."
echo "======================================="

exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --threads 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info