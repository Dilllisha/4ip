from pa.app import *
from vol.vkbot import *

print('готово')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(uvicorn.run(app, host="0.0.0.0", port=80)))
loop.run_until_complete(asyncio.ensure_future(bot()))
loop.close()


    
