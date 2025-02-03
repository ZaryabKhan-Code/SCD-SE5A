"""
Week 6 Demo: Uses static files (CSS) and shows how to serve them in Flask.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title="Week 6 Demo")

if __name__ == "__main__":
    app.run(debug=True)
