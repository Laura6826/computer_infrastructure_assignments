#! /bin/bash

date
echo "Downloading the weather data"
wget -O data/weather/`date +"%Y%m%d_%H%M%S_athenry.json"` https://prodapi.metweb.ie/observations/athenry/today
echo "Weather download complete"
date