import datetime
from app import db
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from app.models.base_model import BaseModel

relationship = db.relationship
Model = db.Model

class Post(BaseModel):
    __tablename__ = 'posts'
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comments = relationship('Comment', backref='post', lazy=True)