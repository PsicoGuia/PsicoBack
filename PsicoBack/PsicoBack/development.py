from PsicoBack.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

import psycopg2
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'development',
        'USER': 'psico',
        'PASSWORD': 'ps1c0gu14',
        'HOST': 'localhost',
        'PORT': '5432',
        #'OPTIONS': {'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,},
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
