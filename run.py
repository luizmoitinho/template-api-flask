from src.config.config import Config
from flask import Flask, request
from flask_cors import CORS
import requests 
import json

from src.service.ServoService import ServoService
from src.service.HealthCheckService import HealthCheckService

servoService = ServoService()
healthcheckService = HealthCheckService()

conf = Config().config
url_api_esp32cam = conf['api_esp32cam']['url']

app = Flask(__name__)
CORS(app)

#============== healthcheck routes =============================
@app.route("/test_connection", methods = ["GET"])
def test_connection():
    healthcheckService.test_connection()

#============== servo routes =============================
@app.route("/servo/rotate", methods =  ["POST"])
def rotate():
    servoService.rotate()
    pass

@app.route("/servo/centralize_target", methods = ["POST"])
def centralize_target():
    servoService.centralize_target((10,5,20),(10,20,12))
    pass

app.run(debug=True)
