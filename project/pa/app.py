from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers.gpt import ___gpt

routers_variables = [value for key, value in globals().items() if key.startswith("___")]

app = FastAPI()

origins = ["*"]
headers = ["*"]
methods = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers)

for router in routers_variables:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=80, reload=True)
