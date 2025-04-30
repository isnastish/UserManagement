from ..ports.user_repository import UserRepository
from ..domain.user import User

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy import Connection


class PostgresUserRepository(UserRepository):
    def __init__(self, conn: "Connection"):
        self._conn = conn

    async def get_user_by_email(self, email: str) -> User:
        query = "SELECT * FROM"
    
    async def get_user_by_id(self, id: str) -> User:
        pass

    async def add_user(self, user: User) -> None:
        pass