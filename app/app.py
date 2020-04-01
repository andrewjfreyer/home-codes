import os 
from flask import Flask, render_template, request

#FLASK
app = Flask(__name__)

@app.route("/q", methods=['GET'])
def query():
    """ This function serves a webpage with appliance config information"""

    q_type = str(request.args.get('type'))
    name = str(request.args.get('name'))

    #only supporting one request time right now
    if (q_type.lower() == "appliance"):

        #render template
        return render_template('index.html',
            name = name)

    return "Unknown error"

#MAIN
if __name__ == "__main__":

    #start the app
    app.run(host='0.0.0.0', port=8080)
