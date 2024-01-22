from pa.app import *
from vol.vkbot import *

print('готово')

loop = asyncio.get_event_loop()

futures = [
    asyncio.ensure_future(uvicorn.run(app, host="0.0.0.0", port=80),
    asyncio.ensure_future(bot())
]

loop.run_until_complete(asyncio.gather(*futures))
loop.close()


    
