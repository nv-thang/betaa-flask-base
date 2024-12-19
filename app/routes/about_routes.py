from flask import Blueprint, render_template
from app.extensions import mongo


about_bp = Blueprint('about', __name__)

@about_bp.route("/about")
def index():
    return render_template("about.html")
