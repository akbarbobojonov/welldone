from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'welldonedb_dev',
        'USER': 'welldone_dev',
        'PASSWORD': 'welldonedev8864',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
