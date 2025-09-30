from typing import TYPE_CHECKING
from models.base import Base
from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
if TYPE_CHECKING:
    from models.users import UsersList
from sqlalchemy import Identity

class Posts(Base):
    __tablename__ = "Posts"
    """Отдельно выношу информации о контактах предполагая что их может быть несколько на пользователя"""

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(start=101, cycle=False),
        primary_key=True,
    )

    user_id : Mapped[int] = mapped_column(
        ForeignKey("UsersList.user_id")
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    body: Mapped[str] = mapped_column(
        String(250),
    )


    User: Mapped["UsersList"] = relationship(    back_populates="posts",)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.user_id}, title={self.title!r}"