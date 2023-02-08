import os
import sys
import time

import requests
from flask import Flask, g, render_template, request, send_from_directory

try:
    import boxes.generators
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
    import boxes.generators

from . import config
from .assets import assets
from .boxes import boxes_app
from .extensions import babel, cache


def create_app(config=config.base_config):
    """Returns an initialized Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app, config)
    register_blueprints(app)
    register_errorhandlers(app)

    @app.before_request
    def before_request():
        """Prepare some things before the application handles a request."""
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index page."""
        return render_template('index.html')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )

    return app


def register_extensions(app, config_):
    """Register extensions with the Flask application."""

    def get_locale():
        """Returns the locale to be used for the incoming request."""
        return request.accept_languages.best_match(config_.SUPPORTED_LOCALES)

    assets.init_app(app)
    try:
        babel.init_app(app, locale_selector=get_locale)
    except TypeError:
        babel.init_app(app)
    cache.init_app(app)


def register_errorhandlers(app):
    """Register error handlers with the Flask application."""

    def render_error(e):
        return render_template('errors/%s.html' % e.code), e.code

    for e in [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED,
    ]:
        app.errorhandler(e)(render_error)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(boxes_app)