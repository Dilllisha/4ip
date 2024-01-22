from pa.app import *
from vol.vkbot import *

print('готово')

if __name__ == "__main__":
  bot()
  uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
    
