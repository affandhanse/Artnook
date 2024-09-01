from .base import *
from .base import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
cwd = os.getcwd()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)-%m&5r2m)1pxe9+ctnm!k%#e_(7892mjbb(_a_5*=m!e0h#q6"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
try:
    import debug_toolbar
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = ["127.0.0.1"]
except ImportError:
    pass
CACHES = {
    "default":{
        "BACKEND":
        "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}


try:
    from .local import *
except ImportError:
    pass
