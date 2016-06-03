from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
    
@app.route("/events")
def events():
    return render_template("events.html")
    
@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)    
    
    
