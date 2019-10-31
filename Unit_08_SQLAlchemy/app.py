# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
import datetime as dt
import numpy as np
from numpy import _distributor_init
from numpy import _mklinit

# Flask Setup
app = Flask(__name__)

# Create the connection engine to the sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False}, echo=True)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<end> <br/>"
    )

# Define what to do when a user hits the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""

    # Calculate the date 1 year ago from last data point
    one_year_duration = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query database for stations
    one_year_duration_q = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > one_year_duration).\
order_by(Measurement.date).all()
    
    # Convert object to a list
    oneyear_prcp_list={}
    for item in one_year_duration_q:
        oneyear_prcp_list[item[0]]=item[1]
    
    # Return jsonified list
    return (jsonify(oneyear_prcp_list))


# Define what to do when a user hits the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return the stations data as json"""
    
    # Query database for list of stations
    list_stations_q = session.query(Station.station).all()
    
    # Convert object to a list
    # station_list={}
    # for item in list_stations_q:
    #     station_list[item[0]]=item[1]
    station_list = list(list_stations_q)
    
    # Return jsonified list
    return (jsonify(station_list))

# Define what to do when a user hits the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature observations data as json"""
    
    # Calculate the date 1 year ago from last data point
    one_year_duration = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query database for list of dates and temperature observations
    tobs_q = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > one_year_duration).all()
    
    # Convert object to a list
    list_tobs = list(tobs_q)
    
    # Return jsonified list
    return (jsonify(list_tobs))

# I COULD NOT MAKE THE FOLLOWING PART TO RUN PROPERLY. THAT IS WHY I KEPT IT AS A COMMENT. 

# Define what to do when a user hits the /api/v1.0/<start> route
# @app.route("/api/v1.0/<start>")
# def start():
#     """Return the `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date data as json"""

#     # Query database for list
#     start_q = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date > start).group_by(Measurement.date).all()
   
#     # Convert object to a list
#     list_start =list(start_q)
    
#     # Return jsonified list
#     return jsonify(list_start)

# @app.route("/api/v1.0/<start>/<end>")
# def start/end():
#     """Return the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date """
    
#     # Query database for list
#     start_end = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    
#     # Convert object to a list
#     start_end_list=list(start_end)
    
#     # Return jsonified list
#     return jsonify(start_end_list)

if __name__ == "__main__":
    app.run(debug=True)