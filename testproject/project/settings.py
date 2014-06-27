DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = dict(
    default=dict(
        ENGINE='django.db.backends.sqlite3',
        NAME='example.db',
        USER='',
        PASSWORD='',
        HOST='',
        PORT='',
    )
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_pony_forms',
    'django_bootstrap3_form',
    'test_app',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'project.urls'

STATIC_URL = '/static/'

SECRET_KEY = 'secret'