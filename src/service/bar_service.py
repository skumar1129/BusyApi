from app import db
from models.bar import Bar
from uuid import uuid4

class BarService():

    def create_bar(self, bar_name, location_id, neighborhood_id=None):
        bar_uuid = str(uuid4())
        if (neighborhood_id is not None):
            bar = Bar(uuid=bar_uuid, name=bar_name.lower(), location_id=location_id, neighborhood_id=neighborhood_id)
        else:
            bar = Bar(uuid=bar_uuid, name=bar_name.lower(), location_id=location_id)
        db.session.add(bar)
        db.session.commit()
        return Bar.query.filter_by(name=bar_name.lower(), location_id=location_id).first()