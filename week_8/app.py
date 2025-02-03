"""
Week 8 Demo: Integrating Flask with SQLAlchemy using SQLite.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week8_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

@app.route("/")
def index():
    return "Week 8 Flask-SQLAlchemy Demo"

if __name__ == "__main__":
    # Create all tables
    db.create_all()
    # Optionally create a user if none exist
    if not User.query.first():
        new_user = User(username="demo_user", email="demo@example.com")
        db.session.add(new_user)
        db.session.commit()
    app.run(debug=True)
