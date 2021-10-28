'''
        Flask APP for Filtering Cities from API 
'''

import json
import requests
from flask import request
from flask import Flask, render_template
from urllib.parse import unquote_plus

app = Flask(__name__)

@app.route("/get_city")
def get_city():
    filtered_cities = []
    number_of_cities = 0
    starting_string = unquote_plus(request.args.get('query').lower()) or ''

    if not starting_string:
        return json.dumps({'cities': filtered_cities, 'no_of_cities' : number_of_cities})

    api_data = requests.get("https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e")
    data = api_data.json()

    cities = [i['name'] for i in data['list']]

    filtered_cities =  [city.strip() for city in cities if city.lower().startswith(starting_string)]
    number_of_cities = len(filtered_cities)

    data = {'cities': filtered_cities, 'no_of_cities' : number_of_cities}

    return json.dumps(data)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=5050)