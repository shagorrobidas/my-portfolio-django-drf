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
    "http://www.shagorrobidas.dev",
]

CSRF_TRUSTED_ORIGINS = [
    "http://shagorrobidas.dev",
    "http://www.shagorrobidas.dev",
    "https://shagorrobidas.dev",
    "https://www.shagorrobidas.dev",
    "http://51.20.17.15",
    "https://51.20.17.15",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = False  # enable only after SSL setup