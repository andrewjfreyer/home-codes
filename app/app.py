import os, json
from flask import Flask, render_template, request

#FLASK
app = Flask(__name__, template_folder='../app')
config = {}

#open configuration file
with open('app/config.json') as json_file:
    config = json.load(json_file)

@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""

    q_type = str(request.args.get('t'))
    name = str(request.args.get('name'))

    #only supporting one request time right now
    if (q_type.lower() == "appliance"):

        #get this devices config
        requested_data = config[name]

        #render template
        return render_template(
            'index.html',
            data = requested_data)
 
    return "Unknown error"

#MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
