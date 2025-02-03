"""
Week 9 Demo: Advanced querying with Flask-SQLAlchemy.
"""

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week9_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))

@app.route("/")
def list_posts():
    # Example: Filter by author, order by title
    posts = Post.query.filter_by(author="John Doe").order_by(Post.title).all()
    # Render in a simple HTML for demo
    template = """
    <h1>Posts by John Doe</h1>
    <ul>
    {% for post in posts %}
        <li><strong>{{ post.title }}</strong>: {{ post.content }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(template, posts=posts)

if __name__ == "__main__":
    db.create_all()
    # Example data seeding
    if not Post.query.first():
        db.session.add(Post(title="First Post", content="Hello World", author="John Doe"))
        db.session.add(Post(title="Second Post", content="Another Post", author="Jane Smith"))
        db.session.add(Post(title="Flask Tips", content="Some content", author="John Doe"))
        db.session.commit()
    app.run(debug=True)
