import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

coro = main()
# <class 'coroutine'>
print(type(coro))

asyncio.run(coro)