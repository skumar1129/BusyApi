from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from uuid import uuid4
from src.models.bar import Bar
from src.models.location import Location
from src.models.user import User
from src.models.rating import Rating
from src.models.neighborhood import Neighborhood
from src.models.busyness import Busyness


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128), nullable=False)
    pic_link = db.Column(db.Text(16383), nullable=True)
    bar_id = db.Column(db.Integer, ForeignKey('bar.id'), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    edited_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.String(128), ForeignKey('user.user_name', ondelete='CASCADE'), nullable=False)
    rating_id = db.Column(db.Integer, ForeignKey('rating.id'), nullable=False)
    anonymous = db.Column(db.Boolean, default=False,nullable=False)
    location_id = db.Column(db.Integer, ForeignKey('location.id'), nullable=False)
    neighborhood_id = db.Column(db.Integer, ForeignKey('neighborhood.id'), nullable=True)
    busyness_id = db.Column(db.Integer, ForeignKey('busyness.id'), nullable=True)
    bar = relationship(
        Bar,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )
    location = relationship(
        Location,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )
    user = relationship(
        User,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )
    rating = relationship(
        Rating,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )
    neighborhood = relationship(
        Neighborhood,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )
    busyness = relationship(
        Busyness,
        backref=backref('posts',
        uselist=True,
        cascade='delete,all')
    )


    def __init__(self, uuid, bar_id, description, created_by, rating_id, anonymous, location_id, neighborhood_id=None, pic_link=None): 
        self.uuid = uuid
        if pic_link is not None:
            self.pic_link = pic_link
        self.bar_id = bar_id
        self.description = description
        self.created_by = created_by
        self.rating_id = rating_id
        self.anonymous = anonymous
        self.location_id = location_id
        if neighborhood_id is not None:
            self.neighborhood_id = neighborhood_id