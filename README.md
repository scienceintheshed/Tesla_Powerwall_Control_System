# Tesla Powerwall Control System
![License](https://img.shields.io/github/license/scienceintheshed/Tesla_Powerwall_Control_System?label=LICENSE&?style=plastic&logo=appveyor)
![Forks](https://img.shields.io/github/forks/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)
![Issues](https://img.shields.io/github/issues/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)

A series of python scripts to control charging of a Powerwall 2

#### Communicating with the Tesla Powerwall 2
This repository uses the python libraries of [Michiel Lowijs](https://github.com/mlowijs/tesla_api/tree/fix-auth) and [Simon Moore](https://github.com/swm11/tesla_api) to gain web access to the endpoints of a Tesla Powerwall 2.  As of December 2020, [Michiel Lowijs'](https://github.com/mlowijs/tesla_api/tree/fix-auth) version now uses AsyncIO and is still under active development so would be the preferred version. 

#### Estimating solar generation.
[Solcast](https://solcast.com) have developed a series of tools that enable owners of solar systems to estimate the upcoming output of their arrays.  These forecasts are based on both ground based and satellite observations of weather patterns and cloud cover and can extend up to 3 days in the future.  Creating a free account allows use of their API to measure your solar systems performance as well as download solar generation estimates.  We use thes following day estimates of solar generation to calculate the shorfall in solar generation over consumption for that day.
