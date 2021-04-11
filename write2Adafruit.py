
import asyncio
import time
import datetime
from tesla_api import TeslaApiClient
from adafruitConfig import *

async def main():
    client = TeslaApiClient('steven@9chd.com', 'Illawarra(99)')

    while True:
        try:
            energy_sites = await client.list_energy_sites()
            batteryReserve = await energy_sites[0].get_backup_reserve_percent()
            batteryPercentage = await energy_sites[0].get_energy_site_live_status_percentage_charged()
            homeUsage = await energy_sites[0].get_home_usage()/1000
            gridUsage = await energy_sites[0].get_grid_usage()/1000
            batteryValue = await energy_sites[0].get_battery_value()/1000
            solarGeneration = await energy_sites[0].get_solar_power()/1000
            availablePower = 13.4 * batteryPercentage / 100

            print(datetime.datetime.now())
            print("Backup reserve percent  = "+"{:.1f}".format(batteryReserve))
            print("Battery percentage      = "+"{:.1f}".format(batteryPercentage))
            print("Home usage              = "+"{:.2f}".format(homeUsage))
            print("Grid usage              = "+"{:.2f}".format(gridUsage))
            print("Battery value           = "+"{:.2f}".format(batteryValue))
            print("Solar generation        = "+"{:.2f}".format(solarGeneration))

            #   The sign of batteryValue determines the charging status of the battery;
            #       - if positive, then the battery is discharging
            #       - zero, then the battery is in standby mode
            #       - if negative, then the battery is charging
            #   The value of batteryValue determines the charge transfer of the battery

            # Here I change the sign of the batteryValue to be more intuative on the graph
            if batteryValue > 0:
                batteryValue = -1 * batteryValue
            elif batteryValue < 0:
                batteryValue = abs(batteryValue)
                
            if batteryValue > .050:
                print("Battery is charging")
                chargingStatus = "Charging"
            elif batteryValue < -0.050:
                print("Battery is discharging")
                chargingStatus = "Discharging"
            else:
                print("Battery is in Standby mode")
                chargingStatus = "Standby"  

            print("")

            aio.send(homeUseage_feed.key, str(homeUsage))
            aio.send(solarOutput_feed.key, str(solarGeneration))
            aio.send(currentCharge_feed.key, str(batteryPercentage))
            aio.send(batteryValue_feed.key, str(batteryValue))
            aio.send(batteryReserve_feed.key, str(batteryReserve))
            aio.send(currentKWHRS_feed.key, str(availablePower))
            aio.send(gridDraw_feed.key, str(gridUsage))
            aio.send(chargingStatus_feed.key, str(chargingStatus))
            aio.send(gridUseage_feed.key, str(gridUsage))

            time.sleep(15)

        except:
            pass

    await client.close()

asyncio.run(main())

