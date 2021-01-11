from app import db
from sqlalchemy import Integer, Column, String
from datetime import datetime

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(128), index=True, unique=True)
    password_hash = Column(String(128), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(512))
    timestamp = Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"
