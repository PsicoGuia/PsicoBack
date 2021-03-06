"""
Django settings for PsicoBack project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ferbi)&sk&4g7iarjpg)#w$1eq=y%92i@8(@_eur^x3m+07go$'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'rest_auth',

    'django_filters',
    'djmoney',
    # 'geoposition',
    'address',
    'widget_tweaks',
    'corsheaders',

    'medic',
    'crm',
    'pqr'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PsicoBack.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [],
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

WSGI_APPLICATION = 'PsicoBack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'psicoguia',
        'USER': 'postgres',
        'PASSWORD': 'ps1c0gu14',
        'HOST': '35.231.147.102',
        'PORT': '5432',
        #'OPTIONS': {'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,},
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#LOGIN_REDIRECT_URL = '/medic'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

DOMAIN = "https://psicoguia.co"
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'files')
MEDIA_URL = '/static/files/'

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCQccce99Xzt23VYwc4GShNc2QC6Zq3dOI'
GOOGLE_API_KEY = 'AIzaSyCQccce99Xzt23VYwc4GShNc2QC6Zq3dOI'
GOOGLE_MAPS_API_KEY = 'AIzaSyCQccce99Xzt23VYwc4GShNc2QC6Zq3dOI'
GOOGLE_API_KEY = 'AIzaSyCQccce99Xzt23VYwc4GShNc2QC6Zq3dOI'

# #TODO
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-relay.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'admin@psicoguia.co'
EMAIL_PORT = 587

# POSTGIS
POST_GIS_MAX_DISTANCE_SEARCH = 500

# ENABLE CORS
CORS_ORIGIN_WHITELIST = (
    'psicoguia.co',
    'www.psicoguia.co'
    'api.psicoguia.co'
)
CSRF_TRUSTED_ORIGINS = (
    'psicoguia.co',
    'www.psicoguia.co',
    'api.psicoguia.co'
)
CORS_ALLOW_HEADERS = default_headers + (
    'access-control-allow-methods',
)