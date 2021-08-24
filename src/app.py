from flask import Flask, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
# from flask_sslify import SSLify
import os
# from config import Config

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{Config.credentials['username']}:{Config.credentials['password']}@/{Config.credentials['schema']}?unix_socket=/cloudsql/{Config.credentials['connectionname']}"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Sahil23!@localhost/app_localdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
cors = CORS(app)
# sslify = SSLify(app
from src.service.busy_service import BusyService as busy_service

@app.route('/barbusyness', methods=['POST'])
@cross_origin()
def create_bar_busyness():
    try:
        busy_service().create_busy_bar(request.json)
        return jsonify({'message': 'successfully created busy bar'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create bar busyness'}), 500


@app.route('/live/busyness', methods=['POST'])
@cross_origin()
def get_live_busyness():
    try:
        busy_service().get_live_busy(request.json)
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create bar busyness'}), 500

@app.route('/average/busyness', methods=['POST'])
@cross_origin()
def get_average_busyness():
    try:
        busy_service().get_average_busy(request.json)
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create bar busyness'}), 500