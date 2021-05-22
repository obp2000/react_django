"""
Django settings for react_django project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from os.path import dirname, abspath, join
from os import environ
from django.conf.locale.ru import formats as ru_formats
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = environ.get("SECRET_KEY", 'sisb5l$#kqbf%e%p9&41fsp!wo1gz37s$vjv8x(a3rm)cdr9m6')

DEBUG = int(environ.get("DEBUG", True))

ALLOWED_HOSTS = environ.get("DJANGO_ALLOWED_HOSTS", 'localhost 127.0.0.1').split(" ")

# SECRET_KEY = 'sisb5l$#kqbf%e%p9&41fsp!wo1gz37s$vjv8x(a3rm)cdr9m6'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# APPEND_SLASH=False

# Application definition

INSTALLED_APPS = [
    'user_auth',
    'test_without_migrations',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'jquery',
    'django.contrib.sites',
    'rest_framework',
    'corsheaders',
    'crispy_forms',
    'extra_views',
    'django_tables2',
    'django_filters',
    "bootstrap4",
    'bootstrap_navbar',
    'django_select2',
    'react_django',
    'city.apps.CityConfig',
    'customer',
    'product',
    'delivery_type',
    'order_item',
    'order',
    'knox',
    'django_extensions',
    # 'djangoformsetjs',
    'dynamic_formsets',
    'widget_tweaks',
    'bootstrap_modal_forms',
    'debug_toolbar',
]

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        # 'react_django_api.apps.PageNumberPaginationWithNumPages',
        'react_django.utils.PageNumberPaginationWithNumPages',
    'PAGE_SIZE': 3,
    'DEFAULT_FILTER_BACKENDS':
        ['rest_framework.filters.SearchFilter'],
    'SEARCH_PARAM': 'term',
    'DATETIME_FORMAT': "%d.%m.%Y %H:%M:%S",
    # 'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    #     'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'knox.auth.TokenAuthentication',
    # ),
}

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'react_django.urls'

BOOTSTRAP_NAVBAR = "react_django.nav_bar:MainNavBar"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bootstrap_navbar.navbars.context_processors.navbar',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'angular2-example_development',
#         'USER': 'postgres',
#         'PASSWORD': '1',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": environ.get("SQL_DATABASE", "angular2-example_development"),
        "USER": environ.get("SQL_USER", "postgres"),
        "PASSWORD": environ.get("SQL_PASSWORD", "1"),
        "HOST": environ.get("SQL_HOST", "127.0.0.1"),
        "PORT": environ.get("SQL_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_KNOX = {
    'TOKEN_TTL': None,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

USE_I18N = True

USE_L10N = True

LOCALE_PATHS = [
    join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('ru', _('Russian')),
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

ru_formats.DATE_FORMAT = 'd.m.Y'
ru_formats.TIME_FORMAT = 'H:i'
ru_formats.DATETIME_FORMAT = 'd.m.Y H:i'
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j E Y H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

TEST_RUNNER = 'react_django.utils.UnManagedModelTestRunner'

LOGIN_REDIRECT_URL = '/'

# AJAX_SELECT_BOOTSTRAP = False

SITE_ID = 1

WSGI_APPLICATION = 'react_django.wsgi.application'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/2",
        "LOCATION": "redis://%s:6379/2" % environ.get("REDIS_HOST", "127.0.0.1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SELECT2_CACHE_BACKEND = "select2"

INTERNAL_IPS = [
    '127.0.0.1',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
