from app import db
from models.neighborhood import Neighborhood
from uuid import uuid4

class NeighborhoodService():

    def create_neighborhood(self, location_id, neighborhood):
        nbhood_uuid = str(uuid4())
        nbhood= Neighborhood(uuid=nbhood_uuid, location_id=location_id, neighborhood=neighborhood.lower())
        db.session.add(nbhood)
        db.session.commit()
        return Neighborhood.query.filter_by(uuid=nbhood_uuid, neighborhood=neighborhood.lower(), location_id=location_id).first()