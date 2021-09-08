from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from uuid import uuid4

class Neighborhood(db.Model):
    __tablename__ = 'neighborhood'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128), nullable=False)
    location_id = db.Column(db.Integer, ForeignKey('location.id'), nullable=False)
    neighborhood = db.Column(db.String(128), nullable=False)

    def __init__(self, uuid, location_id, neighborhood):
        self.uuid = uuid
        self.location_id = location_id
        self.neighborhood = neighborhood