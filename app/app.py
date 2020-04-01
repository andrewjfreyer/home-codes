import os 
from flask import Flask,render_template

#FLASK
app = Flask(__name__)

@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""
    return "success"

#MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
