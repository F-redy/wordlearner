from django.conf import settings

from apps import users
from settings.base import *

INSTALLED_APPS += [
    # extra apps
    'django_extensions',
    'corsheaders',
    'rest_framework',

    # custom apps
    'apps.users.apps.UsersConfig',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Cors headers
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    'https://craft-land-top-student-4ee3c794.koyeb.app',
    'https://drf-on-koyeb.craft-land.koyeb',
]

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

AUTH_USER_MODEL = 'users.User'

if settings.DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]
