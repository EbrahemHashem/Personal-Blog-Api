import datetime
from app import db
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey

relationship = db.relationship
Model = db.Model


class Post(Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comments = relationship('Comment', backref='post', lazy=True)