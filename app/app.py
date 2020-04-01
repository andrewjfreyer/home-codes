import os, json
from flask import Flask, render_template, request

#========== FLASK 
app = Flask(__name__, template_folder='/app/data')
config = {}

#========== LOAD CONFIGURATION FILE
try: 
    #open configuration file
    with open('../app/data/config.json') as json_file:
        config = json.load(json_file)
        print ("Loaded: %s appliance configuration(s).", str(len(config))) 
except:
    print ("Error: Cannot load configuration file or appliance configuration(s).")

#========== DEFINE SIMPLE PRIMARY ROUTE
@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""

    #--- GET VALUES 
    q_type = str(request.args.get('t'))
    name = str(request.args.get('name'))

    #only supporting one request time right now
    if (q_type.lower() == "appliance"):

        #--- LOAD DEVICE CONFIG
        requested_data = config[name]

        #--- RENDER TEMPLATE
        return render_template(
            'index.html',
            data = requested_data)
 
    #INTENTIONALLY EMPTY RESPONSE
    return ('', 204)

#MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
