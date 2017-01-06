SECRET_KEY = 'cat'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'channels',
    'channels.delay'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgiref.inmemory.ChannelLayer',
        'ROUTING': [],
    },
    'fake_channel': {
        'BACKEND': 'channels.tests.test_management.FakeChannelLayer',
        'ROUTING': [],
    }
}

MIDDLEWARE_CLASSES = []
