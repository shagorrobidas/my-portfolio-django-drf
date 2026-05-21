from .base import *
import os


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'my_portfolio'),
        'USER': os.environ.get('DB_USER', 'my_portfolio'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

ALLOWED_HOSTS = [
    "51.20.17.15",
    "shagorrobidas.dev",
    "www.shagorrobidas.dev",
    "localhost",
    "127.0.0.1"
]

CORS_ALLOWED_ORIGINS = [
    "http://shagorrobidas.dev",
    "https://shagorrobidas.dev",
    "http://www.shagorrobidas.dev",
    "https://www.shagorrobidas.dev",
]

CSRF_TRUSTED_ORIGINS = [
    "http://51.20.17.15",
    "https://51.20.17.15",
    "http://shagorrobidas.dev",
    "https://shagorrobidas.dev",
    "http://www.shagorrobidas.dev",
    "https://www.shagorrobidas.dev",
]

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# 🔥 IMPORTANT FIX (your issue was here)
CSRF_COOKIE_SECURE = False   # set TRUE only when HTTPS fully working
SESSION_COOKIE_SECURE = False # set TRUE only when HTTPS fully working

CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"

# -------------------------
# PROXY / SSL
# -------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Enable only after SSL setup
SECURE_SSL_REDIRECT = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'