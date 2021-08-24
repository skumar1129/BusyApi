from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from src.models.user import User
from src.models.drink import Drink

class UserDrink(db.Model):
    __tablename__ = 'user_drink'
    user_name = db.Column(db.String(128), ForeignKey('user.user_name'), primary_key=True)
    drink_id = db.Column(db.Integer, ForeignKey('drink.id'), primary_key=True)
    user = relationship(
        User,
        backref=backref('user_drink'),
        uselist=True
    )
    drink = relationship(
        Drink,
        backref=backref('user_drink'),
        uselist=True
    )

   