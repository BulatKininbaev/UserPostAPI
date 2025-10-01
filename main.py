import uvicorn
from fastapi import FastAPI
from api.views import router
from models.db import sync_engine,sync_session
from api.remote_controller.fetch_data import get_remote_users,get_remote_posts
from api.db_controller.db_methotds import add_users,add_posts,init_models
from fastapi.middleware.cors import CORSMiddleware
import asyncio





app = FastAPI()
origins = [
    # разрешенные источники
    "http://127.0.0.1:8000",
    "http://localhost:63342"
]

app.add_middleware(
    # с начала все запрещаем
    CORSMiddleware,
    # потом начинаем разрешать необходимое
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


async def async_main():
    """Заливка структуры данных и данных с сайта"""
    init_models(sync_engine)
    users_data, posts_data = await  asyncio.gather(
             get_remote_users(),
             get_remote_posts())
    with sync_session() as db_session:
        add_users(db_session, users_data)
        add_posts(db_session, posts_data)


if __name__ == "__main__":
    asyncio.run(async_main())
    uvicorn.run(
         app,
         host="127.0.0.1",
         port=8000,
    )





