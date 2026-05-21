#!/bin/bash

set -e

echo "🚀 Starting Django production container..."

# Wait for DB
echo "⏳ Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ Database connected"

# Migrate
echo "📦 Running migrations..."
python manage.py migrate --noinput

# Static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "🔥 Starting Gunicorn..."

exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 2 \
    --timeout 120 \
    --max-requests 500 \
    --max-requests-jitter 50 \
    --access-logfile - \
    --error-logfile - \
    --log-level warning