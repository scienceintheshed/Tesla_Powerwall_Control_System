import requests
import json
from datetime import datetime
from datetime import timedelta

dateToday = datetime.today()
dateTomorrow = datetime.today() + timedelta(days=1)

#   The requests.get statement along with the url connects to the Solcast site.
res = requests.get('https://api.solcast.com.au/rooftop_sites/YourRooftopSite/forecasts.json?api_key=YourApiKey')

#   Here we convert the data to json format
json_data=res.json()

i=pv=count=0

def theForecast():
    i=0
    pv=0
    count = 0
    while True:
        estimate = json_data['forecasts'][i]['pv_estimate']
        dateTime = json_data['forecasts'][i]['period_end']
        parsedDate = str(dateTime[0:26])
        date_time_obj = datetime.strptime(parsedDate, '%Y-%m-%dT%H:%M:%S.%f')
        localTime = date_time_obj + timedelta(hours=11)
    
        if localTime.hour in range(7, 20):
            pv += (estimate/2)
            count += 1
            if count == 26:
                forecast=pv
                return forecast
                break
        i += 1

forecast = theForecast()
