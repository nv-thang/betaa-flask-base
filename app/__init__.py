from flask import Flask
from app.extensions import init_extensions
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017"
    app.secret_key = "abc-xyz"

    # Khởi tạo extensions
    init_extensions(app)

    # Đăng ký routes
    register_routes(app)

    return app
