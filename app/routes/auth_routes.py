from flask import Blueprint, render_template
from app.extensions import mongo


auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signin")
def index():
    return render_template("signin.html")
