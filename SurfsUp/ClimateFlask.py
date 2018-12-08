###dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
from datetime import date, timedelta
import numpy as np

# Database Set up
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect = True)

#save tables as variables
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

##### Set up Flask
app = Flask(__name__)

#home route
@app.route("/")
def home():
    return ("Welcome to the Hawaii Weather Data API")


#precipition route
@app.route("/api/v1.0/precipitation")
def precip():

    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    rain = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > last_year).order_by(Measurement.date).all()


    rain_totals = []
    for result in rain:
        row = {}
        row["date"] = rain[0]
        row["prcp"] = rain[1]
        rain_totals.append(row)

    return jsonify(rain_totals)


#station route
@app.route("/api/v1.0/stations")
def station():
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)
    

# temps route
@app.route("/api/v1.0/tobs")
def tobs():

	results = session.query(Measurement.tobs).filter(Measurement.date >= "2016-08-23").all()
    year_tobs = list(np.ravel(results))
	return jsonify(year_tobs)

    
#start date route
@app.route("/api/v1.0/<start_date>/")
def trip1(start):

    start = '2016-12-01'
    end =  '2017-8-23'

    trip_data = (session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).
    filter(Measurements.date >= start, Measurements.date <= end).all())
    trip = list(np.ravel(trip_data))
    return jsonify(trip)



#start/end date route
@app.route("/api/v1.0/<start_date>/<end_date>/")
def trip2(start, end):

    start = '2016-12-01'
    end =  '2016-12-14'

    trip_data = (session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).
        filter(Measurements.date >= start).filter(Measurements.date <= end).all())
    trip = list(np.ravel(trip_data))
    return jsonify(trip)

if __name__ == '__main__':
    app.run(debug=True)
