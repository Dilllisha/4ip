from pa.app import *
from vol.vkbot import *
import asyncio

print('готово')

loop = asyncio.get_event_loop()

futures = [
    asyncio.ensure_future(test1()),
    asyncio.ensure_future(test2())
]

loop.run_until_complete(asyncio.gather(*futures))
loop.close()

async def test1():
    uvicorn.run(app, host="0.0.0.0", port=80)

async def test2():
    bot()


    
