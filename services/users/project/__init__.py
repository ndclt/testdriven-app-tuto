import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(script_info=None):
    app = Flask(__name__)
    # set configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    toolbar.init_app(app)
    
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flaks cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
