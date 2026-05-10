from flask import Flask
from app.routes.user import user_bp

from app.database import init_app

def create_app():
    app = Flask(__name__)

    init_app(app)
    # Registrar Blueprints
    app.register_blueprint(user_bp)
    

    return app