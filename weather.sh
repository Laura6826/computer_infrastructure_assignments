#! /bin/bash

date
echo "Downloading the weather data"
wget -O `date +"%Y%m%d_%H%M%S.json"` https://prodapi.metweb.ie/observations/athenry/today
echo "Weather download complete"
date