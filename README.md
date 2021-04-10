# Tesla Powerwall Control System
![License](https://img.shields.io/github/license/scienceintheshed/Tesla_Powerwall_Control_System?label=LICENSE&?style=plastic&logo=appveyor)
![Forks](https://img.shields.io/github/forks/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)
![Issues](https://img.shields.io/github/issues/scienceintheshed/Tesla_Powerwall_Control_System?style=plastic&logo=appveyor)

A series of python scripts to control charging of a Powerwall 2

#### Communicating with the Tesla Powerwall 2
This repository uses the python libraries of [Michiel Lowijs](https://github.com/mlowijs/tesla_api/tree/fix-auth) and [Simon Moore](https://github.com/swm11/tesla_api) to gain web access to the endpoints of a Tesla Powerwall 2.  This particular repo is a branch of the main repo due to Tesla recently changing the authentication protocol.  I have forked the code into this repo to make the cloning simplier.

#### Estimating solar generation.
Solcast have developed a series of tools that enable owners of solar systems to estimate the upcoming output of their arrays.  These forecasts are based on both ground based and satellite observations of weather patterns and cloud cover and can extend up to 3 days in the future.

