from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash

from app.extensions import mongo

screen_bp = Blueprint('screen', __name__)
