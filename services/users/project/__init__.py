import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate


db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()


def create_app(script_info=None):
    app = Flask(__name__)
    CORS(app)
    # set configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flaks cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
