from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from app import db
from models.bar import Bar
from models.busyness import Busyness
from models.day_of_week import DayOfWeek

class BarBusyness(db.Model):
    __tablename__ = 'barbusyness'
    id = db.Column(db.Integer, primary_key=True)
    bar_id = db.Column(db.Integer, ForeignKey('bar.id'), nullable=False)
    day_of_week_id = db.Column(db.Integer, ForeignKey('day_of_week.id'), nullable=False)
    start_hour = db.Column(db.Integer, nullable=False)
    end_hour = db.Column(db.Integer, nullable=False)
    busyness_id = db.Column(db.Integer, ForeignKey('busyness.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    google_live_busyness_id = db.Column(db.Integer, ForeignKey('busyness.id'), nullable=True)
    google_average_busyness_id = db.Column(db.Integer, ForeignKey('busyness.id'), nullable=True)
    bar = relationship(
        Bar,
        backref=backref('barbusyness',
        uselist=True,
        cascade='delete,all')
    )
    how_busy = relationship(
        Busyness,
        foreign_keys=[busyness_id],
        backref=backref('how_busy'),
        uselist=True
    )
    day_of_week = relationship(
        DayOfWeek,
        backref=backref('barbusyness',
        uselist=True,
        cascade='delete,all')
    )
    google_live_busyness = relationship(
        Busyness,
        foreign_keys=[google_live_busyness_id],
        backref=backref('google_live_busyness'),
        uselist=True
    )
    google_average_busyness = relationship(
        Busyness,
        foreign_keys=[google_average_busyness_id],
        backref=backref('google_average_busyness'),
        uselist=True
    )


    def __init__(self, bar_id, day_of_week_id, start_hour, end_hour, busyness_id, google_live_busyness_id=None, google_average_busyness_id=None):
        self.bar_id = bar_id
        self.day_of_week_id = day_of_week_id
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.busyness_id = busyness_id
        if google_live_busyness_id is not None:
            self.google_live_busyness_id = google_live_busyness_id
        if google_average_busyness_id is not None:
            self.google_average_busyness_id = google_average_busyness_id
