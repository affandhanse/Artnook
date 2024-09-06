from .base import *

DEBUG = False
SECRET_KEY = 'mnq-3+7@l32s262r-u)41hv8z3e7!ff0m%6_5-wu8+zks*cpi^'
ALLOWED_HOSTS= ['localhost', 'artnookstudio.mooo.com', '141.148.194.105', '*']



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
        "NAME" : 'rocketman',
        "USER" : 'rocketman',
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
import os

# Email configuration for gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'affandhanse05@gmail.com'
EMAIL_HOST_PASSWORD = 'ldoqhjfvvaezqayw'
DEFAULT_FROM_EMAIL = 'affandhanse05@gmail.com'
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'affandhanse05@gmail.com'


def send_email_with_error_handling(subject, message, from_email, recipient_list, fail_silently=False, connection=None, html_message=None):
    try:
        connection = connection or get_connection(fail_silently=fail_silently)
        email_message = EmailMessage(subject, message, from_email, recipient_list, connection=connection)
        if html_message:
            email_message.content_subtype = "html"
            email_message.body = html_message
        email_message.send()
        logger.info(f"Email sent successfully to {', '.join(recipient_list)}")
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        raise  # Re-raise the exception for further handling


try:
    from .local import *
except ImportError:
    pass
