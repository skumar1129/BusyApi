from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from app import db
from models.user import User
from models.bar import Bar

class UserBar(db.Model):
    __tablename__ = 'user_bar'
    user_name = db.Column(db.String(128), ForeignKey('user.user_name'), primary_key=True)
    bar_id = db.Column(db.Integer, ForeignKey('bar.id'), primary_key=True)
    user = relationship(
        User,
        backref=backref('user_bar'),
        uselist=True
    )
    bar = relationship(
        Bar,
        backref=backref('user_bar'),
        uselist=True
    )

   