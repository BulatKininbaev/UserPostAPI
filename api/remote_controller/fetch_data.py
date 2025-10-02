import aiohttp
from models.users import UsersList
from models.posts  import Posts
from api.remote_controller import USERS_DATA_URL,POSTS_DATA_URL
from json import loads


async def get_data(d_url:str):
    """Асинхронная получение данных с сайта"""
    async with aiohttp.ClientSession() as session:
        async with session.get(d_url) as response:
            return await response.text()


async def get_remote_users()->list[UsersList] | None:
    """Достаем список юзеров для заполнения в базе из и-нета"""
    url_users = await get_data(USERS_DATA_URL)
    out_users = [ UsersList(user_id=j_user['id'],
                                user_name=j_user['username'],
                                name=j_user['name'],
                                user_address=j_user['address']['street']+' '+j_user['address']['city'])
                  for j_user in loads(url_users)]
    return out_users



async def get_remote_posts()->list[Posts] | None:
    """Достаем список постов для заполнения в базе из и-нета"""
    url_posts = await get_data(POSTS_DATA_URL)
    out_posts = [ Posts(user_id=j_user['userId'],
                                title=j_user['title'],
                                body=j_user['body'],
                                id=j_user['id'])
                  for j_user in loads(url_posts)]
    return out_posts



