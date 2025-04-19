from app import db
from sqlalchemy import Column, String
from app.models.base_model import BaseModel

relationship = db.relationship
Model = db.Model

class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)
    comments = relationship('Comment', backref='author', lazy=True)