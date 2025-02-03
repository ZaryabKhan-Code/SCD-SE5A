"""
Week 10 Demo: Handling forms with WTForms (Flask-WTF).
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week10_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretkey"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Create User")

@app.route("/", methods=["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("list_users"))
    return render_template("form.html", form=form)

@app.route("/users")
def list_users():
    users = User.query.all()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
