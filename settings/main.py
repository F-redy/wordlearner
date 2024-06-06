from django.conf import settings

from apps import users
from settings.base import *

INSTALLED_APPS += [
    # extra apps
    'django_extensions',

    # custom apps
    'apps.users.apps.UsersConfig',
]

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
