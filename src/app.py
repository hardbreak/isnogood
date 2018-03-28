# -*- coding: utf-8 -*-

from flask import Flask

def init_views(app: Flask):
    """
    Views have to be initialized here to get working. An import is enough
    """
    with app.app_context():
        from views.index import hello_world
        from views.upload import upload_file
        from views.upload import display_file


def init_app(debug=True) -> Flask:
    """
    Setting up Flask application and register views

    :param debug: app should be running in debug mode
    :type debug: bool
    :return: Flask application with certain settings and registered Blueprints
    :rtype: Flask
    """
    # setup Flask
    app = Flask(__name__)

    app.config.update(
        DEBUG=debug,
        SECRET_KEY='3aa8a825d6575e834457eeb75ca7fece7d6eab15b67efbc1',
    )
    
    init_views(app)

    return app
