
from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    xAxis = request.args.get('xAxis')
    yAxis = request.args.get('yAxis')
    plotData = {
    'x' : getAxis(xAxis), 
    'y':getAxis(yAxis), 
    'mode':'markers', 
    'type':'scatter', 
    'text':infoAboutSongsBuilder(),
    'marker' : {
        'color' : 'rgb(30,215,96)',
        'line' : {
            'color': 'rgb(25,20,20)',
            'width': 1
        }
    }
    }
    return plotData


def getAxis(axis):
    data = pd.read_csv("newBackend/spotify-2023.csv")
    rowSeries = data[axis]
    listOfValues = rowSeries.to_list()
    return listOfValues



def infoAboutSongsBuilder():
    listOfInfo = []
    title = getAxis("track_name")
    artist = getAxis("artist(s)_name")
    year = getAxis("released_year")
    for song in range(len(title)):
        listOfInfo.append(f"{title[song]} - {artist[song]} ({year[song]})")
    return listOfInfo

app.run()