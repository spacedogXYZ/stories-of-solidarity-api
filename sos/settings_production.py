import os
import dj_database_url
from memcacheify import memcacheify

from settings import *

# No debug
DEBUG = False
TEMPLATE_DEBUG = False

# Heroku hosted database & cache
DATABASES['default'] = dj_database_url.config()
CACHES = memcacheify()

# Sendgrid email
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

# SSL
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Allowed host headers
ALLOWED_HOSTS = ['stories-of-solidarity.herokuapp.com', 'storiesofsolidarity.org', 'spacedog.xyz', ]
CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS

# Share session cookies with frontend
# SESSION_COOKIE_DOMAIN = '.storiesofsolidarity.org'

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
