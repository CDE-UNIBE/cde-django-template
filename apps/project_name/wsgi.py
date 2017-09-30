"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""
import sys
import envdir
from os.path import dirname, abspath, join

# Root directory for this project
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Add the apps folder to the path and read the env-vars.
sys.path.append(join(BASE_DIR, 'apps'))
envdir.read(join(BASE_DIR, 'envs'))

# Load the wsgi application with django-configurations.
from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
