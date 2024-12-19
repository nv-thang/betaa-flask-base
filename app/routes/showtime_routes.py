from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from app.extensions import mongo

showtime_bp = Blueprint('showtime', __name__)