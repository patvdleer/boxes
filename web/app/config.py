import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Boxes.py'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secrets')
    SUPPORTED_LOCALES = [
        'en',
        'de',
        'nl',
        'fr',
    ]

    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "Europe/Amsterdam"
    BABEL_TRANSLATION_DIRECTORIES = "translations"


class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
