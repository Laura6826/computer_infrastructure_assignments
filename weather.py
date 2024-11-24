#! /usr/bin/env python

# Imports
import pandas as pd
import datetime as dt

# Download the data
df = pd.read_csv('https://prodapi.metweb.ie/observations/athenry/today')

# Get the current date and time.
filename = dt.datetime.now()

# Create a string from the current date and time.
filename = filename.strftime("%Y%m%d_%H%M%S")
# Prepend data folders, append file extensions.
filename= 'data/project/' + filename + ".csv"

# Show the filename
print(filename)

# Save the data to a CSV file
df.to_csv(filename)
