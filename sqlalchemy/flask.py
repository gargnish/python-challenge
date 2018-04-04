# 1. import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func  
import pandas as pd
engine = create_engine("sqlite:///hawaii.sqlite" , echo=False)
conn = engine.connect()
sess = Session(bind=engine)
import datetime as dt
# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.automap import automap_base
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
## keys are just table names with type definitions
#----importing flask
from flask import Flask, jsonify
c_station = Base.classes.station
c_measurement = Base.classes.measurement

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


def fx_station():
#    with app.app_context():
    v_result = sess.query(c_station).all()
    v_result_list = []
    for i in v_result:
        v_result_dict = {}
        v_result_dict["station"] = i.station
        v_result_dict["name"] = i.name
        v_result_list.append(v_result_dict)
    return jsonify(v_result_list)

        
def fx_prec_temp (v_data_type= 'precipitation' ):
    v_result = sess.query(c_measurement).order_by(c_measurement.date.desc()).first()
    last_date_str = v_result.date
    last_date = dt.date(int(last_date_str.split("-")[0]) , int(last_date_str.split("-")[1] ), int(last_date_str.split("-")[2]) )
    last_year_ago = last_date - dt.timedelta(days=365)
    last_year_ago_str = last_year_ago.strftime("%Y") +'-' +last_year_ago.strftime("%m")+'-' + last_year_ago.strftime("%d")

    # Design a query to retrieve the last 12 months of temperature observation data (tobs).
    sel = [c_measurement.date, 
           func.avg(c_measurement.prcp),
          func.avg(c_measurement.tobs)]
    v_result0 = sess.query(*sel).group_by(c_measurement.date)

    
    v_result = v_result0.filter(c_measurement.date >= last_year_ago_str).filter(c_measurement.date <= last_date_str).all()
    v_result_dict = {}
    for i in v_result:
        (date, prcp, tobs ) = i
        if v_data_type == 'precipitation':
            v_result_dict[date] = round(float(prcp),2)
        else:
            v_result_dict[date] = round(float(tobs),2)

    return jsonify(v_result_dict)



def fx_data_date_range (start_date,  end_date = '' ):
    
    sel = [func.min(c_measurement.tobs), 
       func.avg(c_measurement.tobs),
      func.max(c_measurement.tobs)]
    if end_date != '' :
        v_result = sess.query(*sel).filter(c_measurement.date >= start_date).filter(c_measurement.date <= end_date).first()
    else:
        v_result = sess.query(*sel).filter(c_measurement.date >= start_date).first()

    v_min_temp = round(float(v_result[0]),2)
    v_avg_temp = round(float(v_result[1]),2)
    v_max_temp = round(float(v_result[2]),2)

    
    v_result_list = []
    v_result_dict = {}
    v_result_dict["TMIN"] = v_min_temp
    v_result_dict["TAVG"] = v_avg_temp
    v_result_dict["TMAX"] = v_max_temp
    v_result_list.append(v_result_dict)
    return jsonify(v_result_list)

def fx_index():
    my_html = '<!doctype html>'+chr(10)
    my_html +='<html lang="en">'+chr(10)
    my_html +='<head>'+chr(10)
    my_html +='     <meta charset="UTF-8">'+chr(10)
    my_html +='     <title>Avalable Routes:</title>'+chr(10)

    my_html +='</head>'+chr(10)
    my_html +='<body>'+chr(10)
    my_html +='Avalable Routes:'+chr(10)
    my_html +='<ol><a href = "/api/v1.0/precipitation">/api/v1.0/precipitation</a> - List dates and precipitation observations from the last year</ol>'+chr(10)
    my_html +='<ol><a href = "/api/v1.0/stations">/api/v1.0/stations</a>  - List of stations </ol>'+chr(10)
    my_html +='<ol><a href = "/api/v1.0/tobs">/api/v1.0/tobs</a> - List of Temperature Observations (tobs) for the previous year. </ol>'+chr(10)
    my_html +='<ol><a href = "">/api/v1.0/yyyy-mm-dd</a> - List of the minimum temperature, the average temperature, and the max temperature greater than given start date </ol>'+chr(10)
    my_html +='<ol><a href = "">/api/v1.0/yyyy-mm-dd/yyyy-mm-dd</a> - List of the minimum temperature, the average temperature, and the max temperature between start date (first date paramter) and end date/</ol>'+chr(10)
    my_html +='</body>'+chr(10)
    my_html +='</html>'
    return my_html
	
	
# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
	x = fx_index()
	return x



@app.route("/api/v1.0/precipitation")
def fx_precipitation_call():
	x = fx_prec_temp(v_data_type= 'precipitation')
	return x
#http://127.0.0.1:5000/api/v1.0/precipitation

@app.route("/api/v1.0/stations")
def fx_station_call():
	x = fx_station()
	return x
#http://127.0.0.1:5000/api/v1.0/stations

@app.route("/api/v1.0/tobs")
def fx_temp_call():
	x = fx_prec_temp(v_data_type= 'tobs')
	return x
#http://127.0.0.1:5000/api/v1.0/tobs

@app.route("/api/v1.0/<v_start>")
def fx_data_date_range_call (v_start):
	x = fx_data_date_range (v_start,  '' )
	return x
#http://127.0.0.1:5000/api/v1.0/2016-08-29

@app.route("/api/v1.0/<v_start>/<v_end>")
def fx_data_date_range_call2 (v_start,  v_end ):
	x = fx_data_date_range (v_start,  v_end )
	return x
#http://127.0.0.1:5000/api/v1.0/2016-08-29/2016-08-30


if __name__ == "__main__":
    app.run(debug=True)
