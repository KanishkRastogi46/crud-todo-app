from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

# user model
class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200),  unique=True, nullable=False)
    username = db.Column(db.String(200),  unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    todos = db.relationship('Todo')


# todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))