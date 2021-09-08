from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from src.app import db
from uuid import uuid4

class Bar(db.Model):
    __tablename__ = 'bar'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=True)
    location_id = db.Column(db.Integer, ForeignKey('location.id'), nullable=False)
    type = db.Column(db.String(128), nullable=True)
    neighborhood_id = db.Column(db.Integer, ForeignKey('neighborhood.id'), nullable=True)


    def __init__(self, uuid, name, location_id, neighborhood_id=None, address=None, type=None): # EDIT: took out id, uuid - made address, neighborhood_id, and type optional
        self.uuid = uuid
        self.name = name
        if address is not None:
            self.address = address
        self.location_id = location_id
        if type is not None:
            self.type = type
        self.neighborhood_id = neighborhood_id
