from fastapi import FastAPI
import uvicorn
from router import router_api
from database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

check_app = FastAPI(title='Mongo')
check_app.include_router(router_api)

if __name__ == "__main__":
    uvicorn.run(check_app, host="127.0.0.1", port=8000)
