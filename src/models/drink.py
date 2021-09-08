from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from app import db
from uuid import uuid4

class Drink(db.Model):
    __tablename__ = 'drink'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
