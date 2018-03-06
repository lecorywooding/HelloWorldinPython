#!/usr/bin/env python
from noaaweather import weather

sfWeather = weather.noaa()
sfWeather.getByZip('22903')

print (sfWeather.precipitation.liquid.tomorrow.max.value)
print (sfWeather.temperature.apparent.tomorrow.min.value)
print (sfWeather.temperature.apparent.value)

