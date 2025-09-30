# Схема данных для API
from pydantic import BaseModel,ConfigDict


class UsersReadList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    user_name: str
    name: str
    user_address: str

    def __repr__(self)->str:
        return f"(id={self.user_id},user_name={self.user_name})"


class UsersCreateList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_name: str
    name: str
    user_address: str
