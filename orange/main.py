#!/usr/bin/python3
import errno
import asyncio
from signal import signal, SIGTERM, SIGHUP, pause
from Lib.rpi_lcd import LCD
from Lib.Show_LCD import Show_LCD

show = Show_LCD()


def safe_exit(signum, frame):
    exit(1)


async def create_lcd(bus: int):
    while True:
        try:
            return LCD(address=0x27, bus=bus, width=16, rows=2, backlight=True)
        except OSError as e:
            if e.errno == errno.EIO:
                await asyncio.sleep(10)
            else:
                raise


async def main():
    lcd = await create_lcd(5)
    while True:
        await asyncio.gather(
            show.c1(lcd, "end1", "wlx90de8069de81"),
            show.c2(lcd))


signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)


if __name__ == "__main__":
    asyncio.run(main())
