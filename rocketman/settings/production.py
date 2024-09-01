from .base import *

DEBUG = False
SECRET_KEY = 'mnq-3+7@l32s262r-u)41hv8z3e7!ff0m%6_5-wu8+zks*cpi^'
ALLOWED_HOSTS= ['localhost', 'domainname', '*']



cwd = os.getcwd()
CACHES = {
    "default":{
        "BACKEND":
        "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}
if 'debug_toolbar' in INSTALLED_APPS:
    INSTALLED_APPS.remove('debug_toolbar')

# Remove debug_toolbar middleware if it's in MIDDLEWARE
if 'debug_toolbar.middleware.DebugToolbarMiddleware' in MIDDLEWARE:
    MIDDLEWARE.remove('debug_toolbar.middleware.DebugToolbarMiddleware')



DATABASES ={
    "default":{
        "ENGINE" : 'django.db.backends.postgresql',
        "NAME" : 'artnook',
        "USER" : 'artnook',
        "PASSWORD" : 'almeerah.dhanse',
        "HOST" : 'localhost',
        "PORT" : '',
    }
}

import sentry_sdk

sentry_sdk.init(
    dsn="https://606ae745338b66bf934028d39a811d94@o4507856019914752.ingest.us.sentry.io/4507856030924800",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)



try:
    from .local import *
except ImportError:
    pass
