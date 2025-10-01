# API методы
from fastapi import APIRouter,Request
from models.shemas.users import  UsersReadList,UsersCreateList
from api.db_controller.db_methotds import list_users,list_user_posts,create_user,create_post
from models.db_async import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi.responses import HTMLResponse
from models.shemas.posts import PostReadList
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

templates = Jinja2Templates(directory="templates")

@router.get(
    "/",
    response_model=list[UsersReadList],response_class=HTMLResponse,
)
async def get_users_list(request:Request,session:AsyncSession = Depends(get_async_session)) -> list[UsersReadList]:
    """ Список пользователей """
    results = await list_users(session)
    context = {"request":request,
               "userlist":results}
    return templates.TemplateResponse("userlist.html",context)



@router.get("/posts/{user_id}/",
    response_model=list[PostReadList],
)
async def get_user_posts(user_id:int,session:AsyncSession = Depends(get_async_session)) -> list[PostReadList]:
    """Список постов пользователя """
    return await list_user_posts(session,user_id)

@router.post("/",
    response_model=UsersCreateList)
async def add_user(user:UsersCreateList,session:AsyncSession = Depends(get_async_session)):
    """Создание пользователя"""
    return await create_user(session,user)

@router.post("/posts/",
     response_model=PostReadList)
async def add_post(post:PostReadList,session:AsyncSession = Depends(get_async_session)):
    """Добавление поста пользователя"""
    return await create_post(session,post)

