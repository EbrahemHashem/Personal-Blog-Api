from app.models.base_model import BaseModel
from sqlalchemy import Column, String
from app import db

relationship = db.relationship

class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    posts = relationship('Post', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)