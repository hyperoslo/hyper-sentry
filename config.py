
# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *

import dotenv
dotenv.read_dotenv()
from getenv import env

import os.path

CONF_ROOT = os.path.dirname(__file__)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

####################
## Authentication ##
####################

# Should Sentry allow users to create new accounts?
SENTRY_ALLOW_REGISTRATION = False

# Should Sentry make all data publicly accessible?
SENTRY_PUBLIC = False

# Should Sentry allow users without the 'sentry.change_project' permission to
# make projects globally public?
SENTRY_ALLOW_PUBLIC_PROJECTS = False

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the Caching and Redis settings

#############
## General ##
#############

# The administrative email for this installation.
# Note: This will be reported back to getsentry.com as the point of contact. See
# the beacon documentation for more information.

# SENTRY_ADMIN_EMAIL = 'your.name@example.com'
SENTRY_ADMIN_EMAIL = ''

###########
## Redis ##
###########

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB

import dj_redis_url
REDIS_URL = env('REDIS_URL') or env('REDISTOGO_URL')

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        # Lowercase the dictionary keys generated by dj_redis_url
        0: dict((k.lower(), v) for k, v in dj_redis_url.parse(REDIS_URL).iteritems())
    }
}


###########
## Cache ##
###########

# If you wish to use memcached, install the dependencies and adjust the config
# as shown:
#
#   pip install python-memcached
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }
#
# SENTRY_CACHE = 'sentry.cache.django.DjangoCache'

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'


###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

# CELERY_ALWAYS_EAGER = False
# BROKER_URL = 'redis://localhost:6379'


####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

# SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

############
## Quotas ##
############

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

# SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'


##################
## File storage ##
##################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

# SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
# SENTRY_FILESTORE_OPTIONS = {
#     'location': '/tmp/sentry-files',
# }

################
## Web Server ##
################

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = env('SENTRY_URL_PREFIX', required=True) # No trailing slash!

# List of allowed hosts
ALLOWED_HOSTS = env('ALLOWED_HOSTS', required=True).split(',')

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# and X-Forwarded-Host headers, and uncomment the following settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ['PORT']
SENTRY_WEB_OPTIONS = {
    'workers': env('WEB_CONCURRENCY', required=True),  # the number of gunicorn workers
    'limit_request_line': 0,  # required for raven-js
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

#################
## Mail Server ##
#################

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = env('EMAIL_BACKEND', required=True)
EMAIL_HOST = env('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')
EMAIL_PORT = env('EMAIL_PORT', 25)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', False)

# The email address to send on behalf of
SERVER_EMAIL = env('SERVER_EMAIL', required=True)

###################
## Miscellaneous ##
###################

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = env('SECRET_KEY', required=True)

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY = ''
BITBUCKET_CONSUMER_SECRET = ''

# Force SSL configuration and middleware
SSLIFY_DISABLE = env('SSLIFY_DISABLE', False)
MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
) + MIDDLEWARE_CLASSES
