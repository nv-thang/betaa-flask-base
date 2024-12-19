from flask import Blueprint, render_template
from app.extensions import mongo


home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def index():
    return render_template("home.html")
