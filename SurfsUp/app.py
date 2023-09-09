# Import the dependencies.
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

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
    return(
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Avaiable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()

    prcp_dict = [{"date": date, "percipitation": prcp} for date, prcp in prcp_data]
    
    return jsonify(list(np.ravel(prcp_dict)))

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    results= session.query(Station.station).all()
    results_stations = list(np.ravel(results))
    
    return jsonify(results_stations)

# Tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

    active_station = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= one_year_ago).all()

    most_active_station = [{"date": date, "temp": temp} for date, temp in active_station]
    return jsonify(list(np.ravel(most_active_station)))

# Dynamic route for a given start date
@app.route("/api/v1.0/<start>")
def start_date_temps(start=None):
    sel = [Measurement.date, func.min(Measurement.tobs),func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).group_by(Measurement.date).all()
    
    temps = [{"date": date, "min_temp": min_temp, "avg_temp": avg_temp, "max_temp": max_temp}\
            for date, min_temp, avg_temp, max_temp in results]
    
    return jsonify(list(np.ravel(temps)))

# Dynamic route for a given start and end date
@app.route("/api/v1.0/<start>/<end>")
def date_range_temps(start=None, end=None):
    sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).\
            filter(Measurement.date <= end).group_by(Measurement.date).all()
    temps = [{"date": date, "min_temp": min_temp, "avg_temp": avg_temp, "max_temp": max_temp}\
             for date, min_temp, avg_temp, max_temp in results]
    return jsonify(list(np.ravel(temps)))

if __name__ == '__main__':
    app.run(debug=True)