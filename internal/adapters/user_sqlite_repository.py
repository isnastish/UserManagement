from ..ports.user_repository import UserRepository
from ..domain.user import User

import sqlite3

class SqliteUserRespository(UserRepository):
    def __init__(self):
        # NOTE: For now let's keep all the initialization inside __init__ file.
        pass

    async def get_user_by_email(self, email: str) -> User:
        pass
    
    async def get_user_by_id(self, id) -> User:
        pass

    async def add_user(self, user: User) -> None:
        pass