import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f'started at {time.strftime('%X')}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'finished at {time.strftime('%X')}')

asyncio.run(main())

# 注意这里间隔了3秒
# started at 17:24:00
# hello
# world
# finished at 17:24:03