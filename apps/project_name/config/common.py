from os.path import dirname, join

from configurations import Configuration, values
from django.contrib import messages


class BaseSettings(Configuration):
    """
    Django settings for {{ project_name }} project.

    Generated by 'django-admin startproject' using Django {{ docs_version }}.

    For more information on this file, see
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = join(dirname(dirname(dirname(dirname(__file__)))))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(default=False)

    ALLOWED_HOSTS = values.ListValue(default=['localhost', '127.0.0.1'])

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.gis',
        # Dependencies
        'compressor',
        'sekizai',
        # Custom apps
        # ...
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = '{{ project_name }}.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                join(BASE_DIR, 'templates'),
                # Adding project's template directory (e.g. for base template)
                # instead of adding project as an installed app.
                join(BASE_DIR, 'apps', '{{ project_name }}', 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'sekizai.context_processors.sekizai',
                ],
            },
        },
    ]

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
    DATABASES = values.DatabaseURLValue()

    # Password validation
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
    LANGUAGE_CODE = 'en'
    TIME_ZONE = 'Europe/Zurich'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = join(BASE_DIR, '..', 'static')
    STATICFILES_DIRS = [
        join(BASE_DIR, 'frontend', 'static'),
    ]
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    # Mapping the tags of Django's message framework to Foundation's callout
    # classes
    MESSAGE_TAGS = {
        messages.DEBUG: 'secondary',
        messages.INFO: 'primary',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'alert',
    }
