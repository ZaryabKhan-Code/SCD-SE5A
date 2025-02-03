from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def index():
    return "<h1>Week 13 Main Blueprint</h1>"
