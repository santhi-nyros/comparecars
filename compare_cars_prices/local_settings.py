import os.path
import sys

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#email configuration

ALLOWED_HOSTS = ['*']
#site infos
SITE_NAME = 'compare_car_prices'

#project directories
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static_root") 
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, "templates")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/' 
ADMIN_MEDIA_PREFIX = '/media/admin/'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

TESTSERVER = 'testserver' in sys.argv
TESTING = 'test' in sys.argv or 'testserver' in sys.argv

if 'test' in sys.argv:
    DATABASES = dict (
        default = dict (
            ENGINE = 'django.db.backends.sqlite3',
            TEST = dict (
                #NAME = 'testeracksdb',              # setting NAME here means don't create in-memory sqlite test db
                SERIALIZE = False
            )
        ),
    )
    if TESTSERVER:
        DATABASES ['default'] ['TEST'] ['NAME'] = 'testeracksdb'
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.mysql',
        #         'NAME': 'CompareCarsDB',
        #         'USER': 'Cars_admin',
        #         'PASSWORD': 'Cars_admin',
        #         'HOST': 'localhost',
        #         'PORT': '3306',
        #         'TEST_NAME':'CompareCarsDB_test',
        #     }
        # }


# DATABASES = {
#     'default': {
#         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # Or path to database file if using sqlite3.
#         'NAME': 'comparecarsdb',
#         # The following settings are not used with sqlite3:
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         # Empty for localhost through domain sockets or '127.0.0.1' for
#         # localhost through TCP.
#         'HOST': 'localhost',
#         'PORT': '5432',               
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'CompareCarsDB',
#         'USER': 'Cars_admin',
#         'PASSWORD': 'Cars_admin',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }





# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'secret'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
