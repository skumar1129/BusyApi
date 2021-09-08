from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from app import db
from models.user import User
from models.post import Post
from uuid import uuid4

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    created_by = db.Column(db.String(128), ForeignKey('user.user_name', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)
    edited_at = db.Column(db.DateTime, nullable=True)
    text = db.Column(db.String(128), nullable=False)
    post = relationship(
        Post,
        backref=backref('comments',
        uselist=True,
        cascade='delete,all')
    )
    user = relationship(
        User,
        backref=backref('comments',
        cascade='delete,all')
    )
    