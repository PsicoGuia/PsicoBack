from PsicoBack.development import *
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
