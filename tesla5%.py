import asyncio
from tesla_api import TeslaApiClient

async def main():
    client = TeslaApiClient('username', 'password')

    energy_sites = await client.list_energy_sites()
    reserve = await energy_sites[0].get_backup_reserve_percent()
    await energy_sites[0].set_backup_reserve_percent(5)
    print ("Backup reserve changed to 5%.")

    await client.close()

asyncio.run(main())

