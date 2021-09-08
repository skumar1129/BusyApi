from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db

class User(db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    link_to_prof_pic = db.Column(db.Text(16383), nullable=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256), nullable=True)

   