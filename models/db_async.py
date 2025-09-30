
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from models import config


engine = create_async_engine(
    url=config.db_url_async,
    echo=config.db_echo,
    pool_size=config.sqla_pool_size,
    max_overflow=config.sqla_max_overflow
)


Session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with Session() as session:
        yield session

