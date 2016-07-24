from .common import *

#DEBUG = False
MEDIA_URL = "https://host.local/taiga/media/"
STATIC_URL = "https://host.local/taiga/static/"
ADMIN_MEDIA_PREFIX = "https://host.local/taiga/static/admin/"
SITES["front"]["scheme"] = "https"
SITES["front"]["domain"] = "host.local"


ADMINS = (
   ("less", "less@host.local"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'taiga',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = "theveryultratopsecretkey"

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = True

MEDIA_ROOT = '/var/www/taiga/taiga-back/media'
STATIC_ROOT = '/home/taiga/taiga-back/static'


# EMAIL SETTINGS EXAMPLE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = "tailga@host.local"

from .celery import *

BROKER_URL = 'amqp://taiga:taiga@localhost:5672/taiga-celery'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/taiga-celery'
CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:taiga@localhost:5672/taiga-events"}

# LDAP

INSTALLED_APPS += ["taiga_contrib_ldap_auth"]


LDAP_SERVER = 'ldap://localhost'
LDAP_PORT = 389

# Full DN of the service account use to connect to LDAP server and search for login user's account entry
# If LDAP_BIND_DN is not specified, or is blank, then an anonymous bind is attempated
# LDAP_BIND_DN = 'CN=SVC Account,OU=Service Accounts,OU=Servers,DC=yunohost,DC=org'
# LDAP_BIND_PASSWORD = 'replace_me'   # eg.
# Starting point within LDAP structure to search for login user
LDAP_SEARCH_BASE = 'OU=users,DC=yunohost,DC=org'
# LDAP property used for searching, ie. login username needs to match value in sAMAccountName property in LDAP
LDAP_SEARCH_PROPERTY = 'uid'
LDAP_SEARCH_SUFFIX = None # '@example.com'

# Names of LDAP properties on user account to get email and full name
LDAP_EMAIL_PROPERTY = 'mail'
LDAP_FULL_NAME_PROPERTY = 'displayname'

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec",
#    "import-dump-mode": "1/minute"
#}

# FEEDBACK MODULE (See config in taiga-front too)
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"

# STATS MODULE
#STATS_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second

# SITEMAP
# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second

# CELERY
#from .celery import *
#CELERY_ENABLED = True
#
# To use celery in memory
#CELERY_ENABLED = True
#CELERY_ALWAYS_EAGER = True
