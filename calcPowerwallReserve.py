import asyncio
from tesla_api import TeslaApiClient
import getSolarForecast
import datetime

#   Define and set operational variables
reserve=charge=forecast=solarForecast=shortfall=batteryReserve=0
homeRequirements = 25      # This value is set to whatever your average daily power consumption is in kWh's...recommending adding +10% for contingencies.
powerwallCapacity = 13.4   # This is the accepted capacity of a single Powerwall 2.  For multiple Powerwall 2's simply increment this value. 

async def main():
    try:
        client = TeslaApiClient('YourPowerwallUsername', 'YourPowerwallPassword')
        energy_sites = await client.list_energy_sites()
        reserve = await energy_sites[0].get_backup_reserve_percent()
        charge = await energy_sites[0].get_energy_site_live_status_percentage_charged() / 100 * powerwallCapacity
        await energy_sites[0].set_backup_reserve_percent(reserve+1)

        solarForecast=int(getSolarForecast.forecast)
        shortfall=homeRequirements-(solarForecast+charge-1.34) # The value 1.34 represents 10% of a single Powerwall 2 capacity.  This reserve is a personal choice.

        if shortfall > 13.4:
            # Tesla recommend that the Powerwall should not be charged from the grid to 100%, hence stop at 99%
            await energy_sites[0].set_backup_reserve_percent(99)
        elif shortfall <10:
            # I prefer 10% as a minimum value following overnight charging
            await energy_sites[0].set_backup_reserve_percent(10)
        else:
            # Set reserve to calculated amount
            await energy_sites[0].set_backup_reserve_percent(batteryReserve)

    except:
        pass
        
    await client.close()

asyncio.run(main())

