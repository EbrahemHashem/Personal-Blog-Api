import datetime
from app import db
from sqlalchemy import Column, Integer, DateTime

Model = db.Model

class BaseModel(Model):
    __tablename__ = 'base_model'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
