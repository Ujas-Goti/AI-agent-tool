from flask import Flask
from .routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change-me-in-production"
    app.register_blueprint(routes_bp)
    return app
