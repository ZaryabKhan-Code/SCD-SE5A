"""
Week 11 Demo: Full CRUD on a single model, integrated with Jinja2 templates.
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week11_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route("/")
def home():
    items = Item.query.all()
    return render_template("items_list.html", items=items)

@app.route("/create", methods=["GET", "POST"])
def create_item():
    if request.method == "POST":
        name = request.form["name"]
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create_item.html")

@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == "POST":
        item.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_item.html", item=item)

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
