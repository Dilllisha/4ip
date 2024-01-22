from pa.app import *
from vol.vkbot import *
import asyncio
from multiprocessing import Process

def start():
    uvicorn.run(app, host="0.0.0.0", port=80)
    print("site online")
if __name__ == '__main__':
    p = Process(target=bot)
    b = Process(target=start)
    p.start()
    b.start()
    print("all loaded")




    
