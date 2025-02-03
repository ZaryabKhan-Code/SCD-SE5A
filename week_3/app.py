"""
Week 3 Demo: Simple Flask "Hello World" application.
Run:
    1. pip install flask
    2. flask run (after setting FLASK_APP=app.py or using python app.py)
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask! (Week 3 Demo)"

if __name__ == "__main__":
    # For local development, you can also just run python app.py
    app.run(debug=True)
