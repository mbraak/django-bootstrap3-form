import django


DEBUG = True

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
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_pony_forms',
    'django_bootstrap3_form',
    'test_app',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

if django.VERSION[0:2] <= (1, 9):
    MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'project.urls'

STATIC_URL = '/static/'

SECRET_KEY = 'test_key'

TEMPLATES = [
    dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        APP_DIRS=True,
        OPTIONS=dict(debug=DEBUG)
    )
]

ALLOWED_HOSTS = ['*']
