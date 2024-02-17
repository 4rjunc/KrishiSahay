from flask import Flask
from app.config import load_configurations, configure_logging
from .views import webhook_blueprint

from .utils.database import initialize_database


def create_app():
    app = Flask(__name__)

    # Load configurations and logging settings
    load_configurations(app)
    configure_logging()
    initialize_database()

    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)

    return app
