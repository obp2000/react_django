from os.path import abspath, dirname, join

from decouple import Csv, config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# DEBUG = config("DEBUG")
SECRET_KEY = config("SECRET_KEY")
# ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

# Application definition

INSTALLED_APPS = [
    'user_auth',
    # 'test_without_migrations',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd-party apps
    'corsheaders',
    'crispy_forms',
    'extra_views',
    'django_tables2',
    'django_filters',
    "bootstrap4",
    'bootstrap_navbar',
    'django_select2',
    'dynamic_formsets',
    'widget_tweaks',
    'bootstrap_modal_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_extensions',
    # 'djangoformsetjs',

    # Local
    # 'react_django',
    'customer',
    'product',
    'order_item',
    'order',
    'react_django'
]

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
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

ROOT_URLCONF = 'react_django.urls'

WSGI_APPLICATION = 'react_django.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

USE_I18N = True

USE_L10N = True

LOCALE_PATHS = [join(BASE_DIR, 'locale')]

LANGUAGES = [
    ('ru', _('Russian')),
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

# ru_formats.DATE_FORMAT = 'd.m.Y'
# ru_formats.TIME_FORMAT = 'H:i'
# ru_formats.DATETIME_FORMAT = 'd.m.Y H:i'

DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H:i'

DATETIME_FORMAT = "%d.%m.%Y %H:%M:%S"
DATETIME_INPUT_FORMATS = [DATETIME_FORMAT]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'uploads')

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'knox.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS':
        # 'react_django_api.apps.PageNumberPaginationWithNumPages',
        'react_django.api.pagination.PageNumberPaginationWithNumPages',
    # 'PAGE_SIZE': 8,
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
    'SEARCH_PARAM': 'term',
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS,
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.MultiPartParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.JSONParser',
    # ]
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    #     'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'knox.auth.TokenAuthentication',
    # ),
}

CORS_ORIGIN_ALLOW_ALL = True

BOOTSTRAP_NAVBAR = "react_django.nav_bar:MainNavBar"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{config('REDIS_HOST')}:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SELECT2_CACHE_BACKEND = "select2"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'user_auth.api.serializers.UserLoginSerializer',
    'TOKEN_SERIALIZER': 'user_auth.api.serializers.UserTokenSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": 'user_auth.api.serializers.UserRegisterSerializer'
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": config("SQL_ENGINE"),
#         "NAME": config("SQL_DATABASE"),
#         "USER": config("SQL_USER"),
#         "PASSWORD": config("SQL_PASSWORD"),
#         "HOST": config("SQL_HOST"),
#         "PORT": config("SQL_PORT"),
#     }
# }

# TEST_RUNNER = 'react_django.utils.UnManagedModelTestRunner'

# AJAX_SELECT_BOOTSTRAP = False
