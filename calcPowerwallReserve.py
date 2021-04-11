import asyncio
from tesla_api import TeslaApiClient
import getSolarForecast
import datetime

#   Define and set operational variables
reserve=charge=forecast=solarForecast=shortfall=batteryReserve=0
homeRequirements=25

async def main():
    try:
        client = TeslaApiClient('YourPowerwallUsername', 'UourPowerwallPassword')
        energy_sites = await client.list_energy_sites()
        reserve = await energy_sites[0].get_backup_reserve_percent()
        charge = await energy_sites[0].get_energy_site_live_status_percentage_charged() / 100 * 13.4
        await energy_sites[0].set_backup_reserve_percent(reserve+1)

        solarForecast=int(getSolarForecast.forecast)
        shortfall=homeRequirements-(solarForecast+charge-1.34)
        batteryReserve=abs(shortfall/13.4)*100
        if batteryReserve < 10:
                batteryReserve = 10

            if batteryReserve > 100:
                batteryReserve = 98

        if shortfall > 13.4:
            # Set reserve at 99%
            await energy_sites[0].set_backup_reserve_percent(99)
        elif shortfall <0:
            # Maintain reserve at 10%
            await energy_sites[0].set_backup_reserve_percent(10)
        else:
            # Set reserve to calculated amount
            await energy_sites[0].set_backup_reserve_percent(batteryReserve)

    except:
        pass
        
    await client.close()

asyncio.run(main())

