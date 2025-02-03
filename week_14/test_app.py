"""
Week 14 Demo: Basic Flask and model tests using pytest.
To run tests: pytest
"""

import pytest
from myapp import create_app, db
from myapp.models import User  # Example import if you have a User model

@pytest.fixture
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_homepage(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Week 13 Main Blueprint" in response.data

def test_user_creation(test_client):
    with test_client.application.app_context():
        new_user = User(username="tester", email="test@example.com")
        db.session.add(new_user)
        db.session.commit()
        assert new_user.id is not None
