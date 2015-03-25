import urllib.request
import json
from collections import namedtuple
from datetime import datetime
from bottle import route, view, run
import api_keys

Location = namedtuple("Location", ["name", "code"])
Forecast = namedtuple("Forecast", ["date", "temp", "rain", "wind_deg", "wind_speed", "weather"])

DEFAULT_LOCATION = Location("Tokyo,jp", 13)

@route("/")
@view("index")
def index():
    # get weather forecast
    fs = get_weather_forecasts()
    
    # predict pollen by azure ml
    inputs = []
    for f in fs:
        i = forecast_to_input(f)
        inputs.append(i)
    
    ps = predict(inputs)
    
    data = []
    for i, f in enumerate(fs):
        d = {"forecast": f, "predict": round(ps[i], 1)}
        data.append(d)
    
    return {"data": data}
    
def get_weather_forecasts():
    url = api_keys.FORECAST_URL.format(DEFAULT_LOCATION.name)
    result = None
    forecasts = []
    with urllib.request.urlopen(url) as r:
        body = r.read().decode("utf-8")
        result = json.loads(body)
    
    if result is not None:
        for fd in result["list"]:
            date = datetime.fromtimestamp(fd["dt"])
            f = Forecast(
                date,
                fd["main"]["temp"],
                0 if not "rain" in fd else fd["rain"]["3h"],
                fd["wind"]["deg"],
                fd["wind"]["speed"],
                fd["weather"])
            forecasts.append(f)
    
    return forecasts

def forecast_to_input(f):
    degree_to_direction = lambda x: int((450 - x) % 360 // 22.5)
    
    time = f.date.hour
    prefecture = DEFAULT_LOCATION.code
    pollen = -1 # output value
    wind_direction = degree_to_direction(f.wind_deg)
    wind_direction = wind_direction if wind_direction > 0 else 16  
    params = [time, prefecture, pollen, wind_direction, f.wind_speed, f.temp, f.rain]
    
    # I don't know why, but Azure only accepts integer value
    params = [int(round(p, 0)) for p in params]
    
    return params
    
def predict(inputs):
    data =  {
        "Inputs": {
            "input":
                {
                    "ColumnNames": ["time", "prefecture", "pollen", "wind_direction", "wind_speed", "temperature", "rain"],
                    "Values": inputs
                },
        },
        "GlobalParameters": {}
    }
    body = json.dumps(data).encode("utf-8")
    headers = {"Content-Type":"application/json", "Authorization":("Bearer " + api_keys.AZURE_ML_KEY)}
    result = None
    predicts = []

    req = urllib.request.Request(api_keys.AZURE_ML_URL, body, headers)
    with urllib.request.urlopen(req) as r:
        body = r.read().decode("utf-8")
        result = json.loads(body)
    
    if result is not None:
        values = result["Results"]["output"]["value"]["Values"]
        predicts = [float(v[0]) for v in values]
    
    return predicts
    
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
