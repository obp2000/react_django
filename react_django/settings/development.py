from decouple import Csv, config

from .base import *

DEBUG = True
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

REST_FRAMEWORK['PAGE_SIZE'] = 8

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ['127.0.0.1',]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
    }
}
