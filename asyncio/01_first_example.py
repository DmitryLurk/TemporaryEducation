import asyncio
import time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


async def main():
    await asyncio.gather(tick(),tick(),tick())



if __name__ == '__main__':
    asyncio.run(main())
