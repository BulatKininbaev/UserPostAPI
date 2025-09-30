# Модуль работы с базой данных

from sqlalchemy import select,func,Engine
from sqlalchemy.ext.asyncio import AsyncSession,AsyncEngine
from models.shemas.users import UsersReadList,UsersCreateList
from models.shemas.posts import PostReadList
from models.users import UsersList
from models.posts import Posts
from models.base import Base


def add_users(session:AsyncSession,users:list[UsersList])->None:
    """добавление контактов списком """
    session.add_all(users)
    session.commit()

def add_posts(session:AsyncSession,posts:list[Posts])->None:
    """Добавление постов списком"""
    session.add_all(posts)
    session.commit()

async def create_user(session:AsyncSession,user:UsersCreateList)->UsersCreateList:
    """Создание контакта"""
    a_user= UsersList(**user.model_dump())
    i_result = await session.execute(func.max(UsersList.user_id))
    a_user.user_id = i_result.scalars().one() +1
    session.add(a_user)
    await session.commit()
    return user


async def list_users(session:AsyncSession)->list[UsersReadList]:
    """ Список пользователей """
    statement = (
             select(UsersList)
            .order_by(UsersList.name)
            )
    result = await (session.scalars(statement))
    return list(result.all())


async def list_user_posts(session:AsyncSession,user_id:int)->list[PostReadList]:
    """ Список постов пользователя """
    statement = (
        select(Posts)
        .where(Posts.user_id==user_id)
        .order_by(Posts.title)
    )
    result = await (session.scalars(statement))
    return list(result.all())



def init_models(engine:Engine):
    """ Инициализация модели """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

async def create_post(session:AsyncSession,post:PostReadList)->PostReadList:
    """Создание поста"""
    a_post= Posts(**post.model_dump())
    session.add(a_post)
    await session.commit()
    return post
