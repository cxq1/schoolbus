from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'shoolbus',
#         'USER': 'root',
#         'PASSWORD': 'qq123321',
#         'HOST': 'localhost',
#         'PORT': '3307',
#         'OPTIONS': {
#             "init_command": "SET foreign_key_checks = 0;",
#         }
#
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}