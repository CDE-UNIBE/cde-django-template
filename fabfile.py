from contextlib import contextmanager
from os import environ, path

import configurations
import envdir
from django.conf import settings
from fabric.api import cd, env, run
from fabric.context_managers import prefix
from fabric.contrib import django
from fabric.decorators import task
from fabric.operations import local

# Load the django settings. This needs to read the env-variables and setup
# django-configurations, before the settings_module can be accessed.
envdir.read(path.join(path.dirname(__file__), 'envs'))
configurations.setup()
django.settings_module('{{ project_name }}.settings')


ENVIRONMENTS = {
    'master': {
        'host_string': environ['{{ project_name|upper }}_LIVE_HOST'],
        'source_path': environ['{{ project_name|upper }}_LIVE_PATH'],
        'virtualenv_path': environ['{{ project_name|upper }}_LIVE_VIRTUALENV'],
        'git_remote': 'origin',
        'git_branch': 'master',
        'requirements_file': 'requirements/production.txt',
        'touch_file': environ['{{ project_name|upper }}_LIVE_TOUCH_FILE'],
        'opbeat_app_id': '',
    },
}


@task
def deploy(branch):
    if branch not in ENVIRONMENTS.keys():
        raise BaseException('{} is not a valid branch'.format(branch))

    setup_environment(branch)

    with cd(env.source_path):
        # _set_maintenance('on')
        _update_source()
        _install_dependencies()
        _update_static_files()
        _collectstatic()
        _migrate()
        # _set_maintenance('off')
        _reload_webserver()  # Required as set_maintenance is not called
        _register_deployment()


def _update_source():
    run("git pull %(git_remote)s %(git_branch)s" % env)


def _install_dependencies():
    with virtualenv():
        run("pip install -Ur %(requirements_file)s" % env)


def _update_static_files():
    run('npm install &>/dev/null')
    run('gulp')


def _collectstatic():
    with virtualenv():
        run("python manage.py collectstatic --noinput")


def _migrate():
    with virtualenv():
        run("python manage.py migrate")


def _set_maintenance(switch: str):
    with virtualenv():
        run('python manage.py maintenance %s' % switch)
    _reload_webserver()


def _reload_webserver():
    run('touch %(touch_file)s' % env)


def _register_deployment():
    # Add Opbeat or something else here.
    pass


def setup_environment(environment_name: str):
    """
    Set the proper environment and read the configured values.
    """
    env.environment = environment_name
    for option, value in ENVIRONMENTS[environment_name].items():
        setattr(env, option, value)


@contextmanager
def virtualenv():
    with prefix('source %(virtualenv_path)s' % env):
        yield
