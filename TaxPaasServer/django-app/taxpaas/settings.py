"""
Django settings for sns_prj project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json
from unipath import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(2)
ROOT_DIR = Path(__file__).ancestor(3)
CONF_DIR = ROOT_DIR.child('.django-conf')
STATIC_ROOT = BASE_DIR.child("collected_static")

MEDIA_ROOT = BASE_DIR.child('media')


en_name = os.environ.get("LOGNAME")

# User model
AUTH_USER_MODEL = 'member.CustomUser'

if "USER" in os.environ and os.environ["USER"] == en_name:
    DEBUG = True
else:
    DEBUG = False


# User model
AUTH_USER_MODEL = 'member.CustomUser'

# if "USER" in os.environ and os.environ["USER"] == en_name:
#     DEBUG = True
# else:
#     DEBUG = False

DEBUG = True
if DEBUG:
    config = json.loads(open(CONF_DIR.child("settings_debug.json")).read())
else:
    config = json.loads(open(CONF_DIR.child("settings_deploy.json")).read())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # python - packages
    'debug_toolbar',
    'storages',
    'django_rq',
    'django_rq_dashboard',
    'pyfcm',
    # 'phonenumber_field',
    # django apps
    'communication',
    'taxorg',
    'autoinput',
    'member',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
DATABASES = config['databases']

ROOT_URLCONF = 'taxpaas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'taxpaas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



#Queue Server for Redis, rq
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        # 'PASSWORD': 'qkdwjddl',
        'DEFAULT_TIMEOUT': 360,
        # 'USE_REDIS_CACHE': 'default',
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

# Use redis for caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Use the same redis as with caches for RQ
RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    },
}

# Loggin for redis rq
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rq_scheduler': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# secret key
SECRET_KEY = config['SECRET_KEY']

# email settings
email_config = config['email']
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = email_config['EMAIL_USER_TLS']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATIC_S3 = True
if not DEBUG or STATIC_S3:
    AWS_HEADERS = {
        'Expires': 'Thu, 31 Dec 2199 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }
    AWS_STORAGE_BUCKET_NAME = config['aws']['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = config['aws']['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = config['aws']['AWS_SECRET_ACCESS_KEY']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = "static"
    STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN,
                                        STATICFILES_LOCATION)
    STATICFILES_STORAGE = "taxpaas.custom_storage.StaticStorage"

    MEDIAFILES_LOCATION = "files"
    MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN,
                                       MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'taxpaas.custom_storage.MediaStorage'
    SALT = config['salt']
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    SALT = config['salt']
