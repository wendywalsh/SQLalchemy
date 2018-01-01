import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurements = Base.classes.hawaii_measurement
Stations = Base.classes.hawaii_station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/temperature<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/temperature")
def temperature():
   #return temperature observations for given dates
    temperature =session.query(Measurements.date,Measurements.tobs) \
             .filter(Measurements.date >= '2016-05-01').filter(Measurements.date <= '2017-06-10') \
             .all()
    #Convert the query results to a Dictionary using date as the key and tobs as the value.
    temp_results = []
    for temp in temperature:
        temperature_dict = {}
        temperature_dict["date"] = temp.date
        temperature_dict["tobs"] = temp.tobs
       
        temp_results.append(temperature_dict)

    return jsonify(temp_results)
   


@app.route("/api/v1.0/stations")
def stations():
    # Return list of stations
    stations =session.query(Stations.station,Stations.name).all()

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
#Return a json list of Temperature Observations (tobs) for the previous year
def tobs():
    tobs = session.query(Measurements.tobs) \
             .filter(Measurements.date >= '2016-05-01').filter(Measurements.date <= '2017-06-10') \
             .all()
    
    return jsonify(tobs)


#Return a json list of the minimum temperature, the average temperature, and the max temperature for 
#a given start or start-end range.
##When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>") 
def start_range(start):
    
    #results = session.query(Measurements.date,func.avg(Measurements.tobs),func.min(Measurements.tobs),func.max(Measurements.tobs)) \
    #.filter(Measurements.date >= start).filter(Measurements.date <= end) \
   # .group_by(Measurements.date).all()

    single_date = session.query(Measurements.date,func.avg(Measurements.tobs),func.min(Measurements.tobs),func.max(Measurements.tobs)) \
             .filter(Measurements.date >= start) \
             .group_by(Measurements.date).all()

    return jsonify(single_date)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    range = session.query(Measurements.date,func.avg(Measurements.tobs),func.min(Measurements.tobs),func.max(Measurements.tobs)) \
             .filter(Measurements.date >= start).filter(Measurements.date <= end) \
             .group_by(Measurements.date).all()
    return jsonify(range)



if __name__ == '__main__':
    app.run(debug=True)