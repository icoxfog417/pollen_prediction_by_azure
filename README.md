# pollen prediction by azure

Predict the amount of pollen by Azure Machine Learning.  

## Training data

Download from Hanako-san.

[Hanako-san](http://kafun.taiki.go.jp/index.aspx)

## Model

Neural Network Regression.

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
