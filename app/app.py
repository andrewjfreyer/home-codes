import os, json
from enum import Enum
from flask import Flask, render_template, request

#========== FLASK 
app = Flask(
    __name__, 
    template_folder='/app/data', 
)

#========== DEFINE CLASS OF TYPES 
class ConfigurationType(Enum):
    APPLIANCE = 1

#========== LOAD CONFIGURATION FILE
config = {}
try: 
    with open('../app/data/config.json') as json_file:
        config = json.load(json_file)
        print ("Loaded: " + str(len(config)) + " appliance configuration(s) from config.json.") 
except:
    print ("Error: Cannot load config.json.")

#========== DEFINE SIMPLE PRIMARY ROUTE
@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""

    #--- GET VALUES 
    config_type = str(request.args.get('t'))
    config_id = str(request.args.get('id'))

    #only supporting one request time right now
    if (int(config_type) == ConfigurationType.APPLIANCE):

        #--- LOAD DEVICE CONFIG
        requested_data = config[config_id]

        #--- RENDER TEMPLATE
        return render_template(
            'index.html',
            data = requested_data)
 
    print (config_type)
    print (config_id)

    print ("WORKING????!!")

    #INTENTIONALLY EMPTY RESPONSE
    return ('', 204)

#MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
