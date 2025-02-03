"""
Week 4 Demo: Demonstrates multiple routes, dynamic URLs, and handling GET/POST.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Week 4 Demo!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        data = request.form.get("data_field", "")
        return f"You submitted: {data}"
    return """
    <form method="POST" action="/submit">
        <input type="text" name="data_field" placeholder="Enter something" />
        <input type="submit" value="Submit" />
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
