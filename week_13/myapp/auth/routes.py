from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/login")
def login():
    return "<h1>Login Page</h1>"
