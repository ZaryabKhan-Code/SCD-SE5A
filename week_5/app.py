"""
Week 5 Demo: Uses Jinja2 templates for rendering HTML with variables.
Folder structure:
- app.py
- templates/
    - base.html
    - index.html
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Passing a variable to the template
    return render_template("index.html", title="Week 5 Demo", user="Student")

if __name__ == "__main__":
    app.run(debug=True)
