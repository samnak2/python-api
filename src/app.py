from flask import Flask
from .config import app_config
def create_app(env_name):
    # Create app
    # app initialization
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    @app.route("/prices", methods=["GET"])
    def index():
        # example endpoint
        return "api"
    return app