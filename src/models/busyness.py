from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from app import db

class Busyness(db.Model):
    __tablename__ = 'busyness'
    id = db.Column(db.Integer, primary_key=True)
    busyness = db.Column(db.String(128), nullable=False)