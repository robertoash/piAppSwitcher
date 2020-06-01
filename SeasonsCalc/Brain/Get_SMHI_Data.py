######### Input

import requests
import json
from SeasonsCalc.Brain import extract_values
from datetime import datetime
import numpy as np

datesutc = []
tempstablefull_sorted = []
tempsfloatfull = []
temps = []

## Get data from SMHI API
#tdata = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/97200/period/latest-months/data.json") # Parameter 1 = Lufttemperatur momentanvärde, 1 gång/tim # Station 97200 = Stockholm Bromma 
tdata = requests.get("https://opendata-download-metobs.smhi.se/api/version/latest/parameter/2/station/97200/period/latest-months/data.json")  # Parameter 2 = Lufttemperatur medelvärde 1 dygn, 1 gång/dygn, kl 00 # Station 97200 = Stockholm Bromma


######## Preparation


datesfull = extract_values.extract_values(tdata.json(), 'ref')   # Extract dates from JSON
tempsfull = extract_values.extract_values(tdata.json(), 'value') # Extract temp values from JSON
for x in tempsfull:
    tempsfloatfull.append(float(x))

#tempstablefull = dict(zip(datesfull, tempsfull)) #Zipped Full in case we need to see it

npdates = np.array(datesfull) # onvert to numpy array
nptemps = np.array(tempsfloatfull) # Convert to numpy array
npinds = npdates.argsort()    # Create index based on date sorting
temps_sorted = nptemps[npinds] # Sort temps based on index
tempstablefull_sorted = np.array(list(zip(npdates, temps_sorted))) # Rezip with correct sorting

tempstable_latest = tempstablefull_sorted[-7:,]
tempslist = list(tempstable_latest[0:,1])
for x in tempslist:
    temps.append(float(x))


#print(nptempstablefull_sorted[1,])

######## Calculation


######## Output

#print(tempstablefull)
#print(temps)
#print(tempslist)
#print(tempstable_latest)
