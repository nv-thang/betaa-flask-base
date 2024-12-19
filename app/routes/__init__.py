from .movie_routes import movie_bp
from .home_routes import home_bp
from .about_routes import about_bp
from .contact_routes import contact_bp
from .screen_routes import screen_bp
from .showtime_routes import showtime_bp
from .auth_routes import auth_bp


def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(screen_bp)
    app.register_blueprint(showtime_bp)
    app.register_blueprint(auth_bp)
