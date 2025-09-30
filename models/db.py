from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from models import config

sync_engine = create_engine(
    url=config.db_url,
    echo=config.db_echo,
)


sync_session = sessionmaker(bind=sync_engine)
