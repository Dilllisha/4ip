from pa.app import *
from vol.vkbot import *
import asyncio
from multiprocessing import Process

def start():
    uvicorn.run(app, host="0.0.0.0", port=80)
    print("site online")
    
vkbot = Process(target=bot())
server = Process(target=start())
vkbot.start()
server.start()




    
