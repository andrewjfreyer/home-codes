import os, json
from enum import IntEnum
from flask import Flask, render_template, request

#========== VERSION 
version='0.1.3'


#========== FLASK 
app = Flask(
    __name__, 
    template_folder='/', 
)

#========== DEFINE CLASS OF TYPES 
class ConfigurationType(IntEnum):
    APPLIANCE = 1

#========== DEFINE SIMPLE PRIMARY ROUTE
@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""

    #--- LOAD CONFIG 
    config = {}
    
    #try: 
    with open('../config.json') as json_file:
        config = json.load(json_file)
        print ("Loaded: " + str(len(config)) + " appliance configuration(s) from config.json.") 
    #except:
    #    return ('Error: Configuration file not found.')

    #--- GET VALUES 
    config_type = str(request.args.get('t'))
    config_id = str(request.args.get('id'))

    #only supporting one request time right now
    if (int(config_type) == ConfigurationType.APPLIANCE):

        #--- LOAD DEVICE CONFIG
        try:
            requested_data = config[config_id]

            #--- RENDER TEMPLATE
            return render_template(
                'index.html',
                data = requested_data)
        except:
            return ('Error: Configuration file cannot be read. Key ['+ config_id +'] not found in configuration.')

    #--- EMPTY RESPONSE
    return ('', 204)

#========== MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
