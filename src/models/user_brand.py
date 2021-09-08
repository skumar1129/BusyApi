from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from src.models.user import User
from src.models.brand import Brand

class UserBrand(db.Model):
    __tablename__ = 'user_brand'
    user_name = db.Column(db.String(128), ForeignKey('user.user_name'), primary_key=True)
    brand_id = db.Column(db.Integer, ForeignKey('brand.id'), primary_key=True)
    user = relationship(
        User,
        backref=backref('user_brand'),
        uselist=True
    )
    brand = relationship(
        Brand,
        backref=backref('user_brand'),
        uselist=True
    )


  