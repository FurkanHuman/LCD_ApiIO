from Lib.Get_Info import Get_Info
import asyncio


class Show_LCD:
    def __init__(self):
        self.info = Get_Info()

    async def c1(self, lcd, interface_wired: str, interface_wireless: str):
        lcd.text("Kablolu Ip:", 1)
        await asyncio.sleep(3)

        lcd.text(f"{await self.info.get_ip(f'{interface_wired}')}", 1)
        await asyncio.sleep(7)

        lcd.text("Kablosuz Ip:", 1)
        await asyncio.sleep(3)

        lcd.text(f"{await self.info.get_ip(f'{interface_wireless}')}", 1)
        await asyncio.sleep(7)

    async def c2(self, lcd):
        lcd.text(f"CPU S. :{await self.info.get_cpu_temperature()}°C", 2)
        await asyncio.sleep(5)

        lcd.text(f"CPU K. :{self.info.get_cpu_usage()}%", 2)
        await asyncio.sleep(5)

        lcd.text(f"Ram K. :{self.info.get_ram_usage()}", 2)
        await asyncio.sleep(5)

        lcd.text(f"Docker's: {self.info.get_running_docker_containers()}", 2)
        await asyncio.sleep(5)
