import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'my_portfolio'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Add your VPS IP and domain name here
ALLOWED_HOSTS = ["51.20.17.15", "shagorrobidas.dev", "www.shagorrobidas.dev", "localhost", "127.0.0.1"]

# For production CORS, you should restrict this to your domain if it's an API, 
# but for a portfolio it's generally fine, or specify exact origins:
# CORS_ALLOWED_ORIGINS = ["https://shagorrobidas.dev"]
CORS_ALLOW_ALL_ORIGINS = True

# Security settings for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Optionally, redirect all HTTP traffic to HTTPS (Handled by Nginx mostly, but good to have)
# SECURE_SSL_REDIRECT = True
