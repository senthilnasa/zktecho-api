
from flask import Flask
from .middleware import validate_api_credentials

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
