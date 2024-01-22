from pa.app import *
from vol.vkbot import *
import asyncio
from multiprocessing import Process

def run():
    uvicorn.run(app, host="0.0.0.0", port=80)
    
if __name__ == "__main__":
    Process(target=bot).start()
    Process(target=run).start()




    
