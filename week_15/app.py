"""
Week 15 Demo: Custom error pages and basic logging setup.
"""

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template

app = Flask(__name__)

# Logging Configuration
handler = RotatingFileHandler("week15_app.log", maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"404 error: {e}")
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):
    app.logger.error(f"500 error: {e}")
    return render_template("500.html"), 500

@app.route("/")
def home():
    return "Week 15 - Error Handling & Logging Demo"

if __name__ == "__main__":
    app.run(debug=True)
