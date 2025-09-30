# Схема данных для API
from pydantic import BaseModel,ConfigDict


class PostReadList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    title: str
    body: str
