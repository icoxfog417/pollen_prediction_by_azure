# pollen prediction by azure

Predict the amount of pollen by Azure Machine Learning.  

## Training data

Download from Hanako-san.

[Hanako-san](http://kafun.taiki.go.jp/index.aspx)

## Model

Liner Regression Model.

[pollen prediction](http://gallery.azureml.net/Details/c5ffa1f9ae6c4f068d8032b5ff7e25b2)

* input
 * time(1-24)
 * Prefecture(1-47)
 * wind direction(0-16)
 * wind speed
 * temperature
 * rain(mm/h)

* output
 * amount of pollen (number of pollen/m3)


## As Application

1. Predict the weather by [OpenWeatherMap API](http://openweathermap.org/forecast#data)
2. Predict the amount of poller by weather data of 1.
3. Then, you can get "poller amount prediction".

To run the application.

```
python application.py
```

! Before executing the script, You have to create `api_keys.py` as below.

```
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?q={0}&units=metric"
AZURE_ML_URL = "<Your API URL>"
AZURE_ML_KEY = "<Your API's Key>"
```
