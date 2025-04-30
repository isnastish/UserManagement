from ..domain.user import User

from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        ...
    
    @abstractmethod
    async def get_user_by_id(self, id: str) -> User:
        # NOTE: ID could be a uuid
        ...

    @abstractmethod
    async def add_user(self, user: User) -> None:
        ...