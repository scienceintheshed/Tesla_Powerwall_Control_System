# Tesla Powerwall Control System
![License](https://img.shields.io/github/license/scienceintheshed/Tesla_Powerwall_Control_System?label=LICENSE&?style=plastic&logo=appveyor)
![Forks](https://img.shields.io/github/forks/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)
![Issues](https://img.shields.io/github/issues/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)

A series of python scripts to control charging of a Powerwall 2.  This is my first public repository so please be nice to me.

## Background.
The Tesla Powerwall 2 is a very good battery system for storing excess generated solor power that can then be used once the sun has set.  An additional feature that does not appear to be widely used is the ability to charge the battery from the grid.  This is particuliarly useful is you are on a Time of Use (TOU) tarrif where electricity charges are lower between the hours of say 10:00pm to 7:00am.

## Communicating with the Tesla Powerwall 2.
This repository uses the python libraries of [Michiel Lowijs](https://github.com/mlowijs/tesla_api/tree/fix-auth) and [Simon Moore](https://github.com/swm11/tesla_api) to gain web access to the endpoints of a Tesla Powerwall 2.  As of December 2020, [Michiel Lowijs'](https://github.com/mlowijs/tesla_api/tree/fix-auth) version now uses AsyncIO and is still under active development so is the preferred version. 

## Estimating solar generation.
[Solcast](https://solcast.com) have developed a series of tools that enable owners of solar systems to estimate the upcoming output of their arrays.  These forecasts are based on both ground based and satellite observations of weather patterns and cloud cover and can extend up to 3 days in the future.  Creating a free account allows use of their API to measure your solar systems performance as well as download solar generation estimates.  We use these following day estimates of solar generation to calculate the shorfall in solar generation over consumption for that day.

## Description of Python Scripts
### tesla5%.py
This is the simple script that is run during the morning to reset the Powerwall 2's reserve for power outages.  This value can be set to any value from 0% to 100% depending on circumstances.  Typical values are in the range 5% - 10%.  From experience, a reserve of 5% provides sufficient backup power for our location.  For locations that have more frequent or prolonged grid outages, this value should be increased.

### getSolarForecast.py
This script gets the next days solar generation prediction from [Solcast](https://solcast.com).  The script is called from calcPowerwallReserve.py and simply returns the predicted solar generation in kW's.

### calcPowerwallReserve.py
This script calculates the shortfall (if any) in the next days solar generation over consumption.  Once the shortfall is calculated, the value of the Powerwall reserve is changed.

### write2Adafruit.py
This script is run continuously to update the adafruit.io dashboard.  There is ample documentation available for creating an Adafruit dashboard so it will not be covered here.  Suffice to say that a free account is all that is needed if you wish to visualise the status of your system.

## Suggested mode of operation.
Whilst it is possible to incorporate all the above scripts into one module, I have found it better to schedule tesla5%.py, and calcPowerwallReserve.py using either Windows Task Scheduler (if this is run on a Windows PC) or create cron jobs if Raspberry Pi boards are used.
