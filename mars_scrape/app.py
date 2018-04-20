import scrape_mars as code
from flask import Flask, jsonify, render_template

#global v_scrape_fact

app = Flask(__name__) 

# Define what to do when a user hits the index route
@app.route("/")
def welcome():
	v_latest_doc= code.fx_fetch_latest_time_list(1)
	v_latest_id = v_latest_doc[0]['_id']
	x= code.fx_fetch_doc(v_latest_id)
	y= code.fx_fetch_latest_time_list(5)
	z= code.dt.datetime.strftime(x['list_time'], '%Y-%m-%d %H:%M:%S')
	return render_template("index.html", v_dict=x , v_time_list=y , v_list_time_str= z)

@app.route("/scrape")
def fx_scrape_call():
	x = code.fx_scrape()
	y= code.fx_fetch_latest_time_list(5)
	z= code.dt.datetime.strftime(x['list_time'], '%Y-%m-%d %H:%M:%S')
	return render_template("index.html", v_dict=x, v_time_list=y , v_list_time_str= z)
#http://127.0.0.1:5000/scrape

@app.route("/archive/<my_oject_id>")
def fx_archive_call (my_oject_id):
	x= code.fx_fetch_doc(code.ObjectId(my_oject_id))
	y= code.fx_fetch_latest_time_list(5)
	z= code.dt.datetime.strftime(x['list_time'], '%Y-%m-%d %H:%M:%S')
	return render_template("index.html", v_dict=x, v_time_list=y , v_list_time_str= z)
#http://127.0.0.1:5000/archive/5ad68c10e7191b637c3992d1

if __name__ == "__main__":
    app.run(debug=True)

	
	