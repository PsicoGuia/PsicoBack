from PsicoBack.development import *
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'development',
        'USER': 'psico',
        'PASSWORD': 'ps1c0gu14',
        'HOST': '172.17.0.1', 
        'PORT': '5432',
        #'OPTIONS': {'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,},
    }
}
