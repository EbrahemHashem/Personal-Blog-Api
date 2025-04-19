from app import db
from sqlalchemy import Column, Integer, Text, ForeignKey
from app.models.base_model import BaseModel

Model = db.Model

class Comment(BaseModel):
    __tablename__ = 'comments'
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)