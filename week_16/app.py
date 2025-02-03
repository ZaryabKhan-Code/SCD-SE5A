"""
Week 16 Demo: Simple caching to optimize repeated route responses.
"""

from flask import Flask
from flask_caching import Cache
import time

app = Flask(__name__)
# Config for Flask-Caching
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)

@cache.cached(timeout=10)
@app.route("/slow")
def slow():
    time.sleep(3)  # Simulate a slow function
    return "This response was delayed, but it's cached for 10 seconds!"

if __name__ == "__main__":
    app.run(debug=True)
