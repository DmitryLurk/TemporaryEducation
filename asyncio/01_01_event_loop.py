import asyncio
import time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


async def main():
    await asyncio.gather(tick(), tick(), tick())



if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
        #loop.run_until_complete(main())
        print('coroutines have finished')
    except KeyboardInterrupt:
        print('manual closed')

    finally:
        loop.close()
        print('loop is closed')