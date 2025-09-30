
from typing import TYPE_CHECKING
from models.base import Base
from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped, mapped_column,relationship
if TYPE_CHECKING:
    from models.posts import Posts

class UsersList(Base):
    __tablename__ = "UsersList"
    """Пользователи (заполняю только часть информации с сайта)  """

    user_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    user_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    user_address: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    posts: Mapped[list["Posts"]] = relationship(        back_populates="User",    )

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.user_id}, username={self.user_name!r}, address={self.user_address!r}, full_name={self.name!r})"
