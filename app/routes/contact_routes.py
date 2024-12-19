from flask import Blueprint, render_template
from app.extensions import mongo


contact_bp = Blueprint('contact', __name__)

@contact_bp.route("/contact")
def index():
    return render_template("contact.html")
