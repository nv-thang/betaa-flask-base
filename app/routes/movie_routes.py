from flask import Blueprint, request, jsonify, render_template
from app.models.movie import Movie
from app.extensions import mongo

movie_bp = Blueprint('movie', __name__)