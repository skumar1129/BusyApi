from flask import request, jsonify
import datetime
from src.app import db
from src.models.barbusyness import BarBusyness
from src.models.bar import Bar
from src.models.location import Location
from src.models.neighborhood import Neighborhood
from src.models.busyness import Busyness
from src.service.neighborhood_service import NeighborhoodService as neighborhood_service
from src.service.bar_service import BarService as bar_service


class BusyService():
    
    def create_busy_bar(self, body):
        location = Location.query.filter_by(location=body['location']).first()
        if (body['neighborhood']) is not None:
            neighborhood = Neighborhood.query.filter_by(neighborhood=body['neighborhood'].lower()).first()
            if neighborhood is None:
                neighborhood = neighborhood_service().create_neighborhood(location_id=location.id, neighborhood=body['neighborhood'])
            bar = Bar.query.filter_by(location_id=location.id, neighborhood_id=neighborhood.id, name=body['bar'].lower()).first()
            if bar is None:
                bar = bar_service().create_bar(bar_name=body['bar'], location_id=location.id, neighborhood_id=neighborhood.id)
        else:
            bar = Bar.query.filter_by(location_id=location.id, name=body['bar'].lower()).first()
            if bar is None:
                bar = bar_service().create_bar(bar_name=body['bar'], location_id=location.id)
        day_of_week_id = datetime.datetime.now().isoweekday()
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        if minute > 30:
            start_hour = hour + 1
        else:
            start_hour = hour
        end_hour = start_hour + 1
        google_live_busyness = None
        if (body['google_live_busyness']):
            google_live_busyness = body['google_live_busyness']   
        busyness = Busyness.query.filter_by(busyness=body['busyness']).first()
        busyness_id = busyness.id
        google_average_busyness = None 
        if (body['google_average_busyness']):
           google_average_busyness = body['google_average_busyness']
        busy_bar = BarBusyness(bar_id=bar.id, day_of_week_id=day_of_week_id, start_hour=start_hour, end_hour=end_hour, busyness_id=busyness.id, google_average_busyness_id=google_average_busyness, google_live_busyness_id=google_average_busyness)
        db.session.add(busy_bar)
        db.session.commit()
        

    def get_live_busy(self, body):
        location = Location.query.filter_by(location=body['location']).first()
        if (body['neighborhood']):
            neighborhood = Neighborhood.query.filter_by(neighborhood=body['neighborhood'].lower()).first()
            bar = Bar.query.filter_by(location_id=location.id, neighborhood_id=neighborhood.id, name=body['bar'].lower()).first()
        else:
            bar = Bar.query.filter_by(location_id=location.id, name=body['bar'].lower()).first()
        if bar is None:
            return 'Could Not Find Bar'
        day_of_week_id = datetime.datetime.now().isoweekday()
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        if minute > 30:
            start_hour = hour + 1
        else:
            start_hour = hour
        end_hour = start_hour + 1
        thirty_before = datetime.datetime.now() - datetime.timedelta(minutes=30)
        busyness_data = BarBusyness.query.filter_by(bar_id=bar.id).filter(BarBusyness.created_at>=thirty_before).all()
        busyness_count = 0
        busyness_score = 0
        for data in busyness_data:
            busyness_score += (data.busyness_id / 3)
            if data.google_live_busyness_id:
                busyness_score += (data.google_live_busyness_id / 3)
            if data.google_average_busyness_id:
                busyness_score += (data.google_average_busyness_id / 3)
            busyness_count += 1
        if busyness_count == 0:
            busyness = 'No Information For This Time'
        else:
            busyness = self.get_busyness(busyness_score / busyness_count)
        return busyness
         
    
    def get_average_busy(self, body):
        location = Location.query.filter_by(location=body['location']).first()
        if (body['neighborhood']):
            neighborhood = Neighborhood.query.filter_by(neighborhood=body['neighborhood'].lower()).first()
            bar = Bar.query.filter_by(location_id=location.id, neighborhood_id=neighborhood.id, name=body['bar'].lower()).first()
        else:
            bar = Bar.query.filter_by(location_id=location.id, name=body['bar'].lower()).first()
        if bar is None:
            return 'Could Not Find Bar'
        day_of_week_id = datetime.datetime.now().isoweekday()
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        if minute > 30 and hour != 23:
            start_hour = hour + 1
        elif minute > 30 and hour == 23:
            start_hour = 0
            day_of_week_id = (day_of_week_id + 1 if day_of_week_id != 7 else 1)
        else:
            start_hour = hour
        end_hour = start_hour + 1
        busyness_data = BarBusyness.query.filter_by(bar_id=bar.id, day_of_week_id=day_of_week_id, start_hour=start_hour, end_hour=end_hour).all()
        busyness_count = 0
        busyness_score = 0
        for data in busyness_data:
            busyness_score += (data.busyness_id / 3)
            if data.google_live_busyness_id:
                busyness_score += (data.google_live_busyness_id / 3)
            if data.google_average_busyness_id:
                busyness_score += (data.google_average_busyness_id / 3)
            busyness_count += 1
        if busyness_count == 0:
            busyness = 'No Information For This Time'
        else:
            busyness = self.get_busyness(busyness_score / busyness_count)
        return busyness
    
    def get_busyness(self, score):
        busyness = round(score)
        busy_dict = {
            1: 'Dead AF',
            2: 'Some Crowd',
            3: 'Lively Enough',
            4: 'There Are Lines',
            5: 'Can’t Move'
        }
        return busy_dict.get(busyness)
        
         