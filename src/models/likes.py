from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from src.models.post import Post
from src.models.user import User

class Likes(db.Model):
    __tablename__ = 'likes'
    user_name = db.Column(db.String(128), ForeignKey('user.user_name', ondelete='CASCADE'), primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), primary_key=True)
    like = db.Column(db.Boolean, default=False)
    post = relationship(
        Post,
        backref=backref('like',
        uselist=True,
        cascade='delete,all')
    )
    user = relationship(
        User,
        backref=backref('like',
        uselist=True,
        cascade='delete,all')
    )

  