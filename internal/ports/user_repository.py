from ..domain.user import UserData

from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> UserData:
        ...
    
    @abstractmethod
    async def get_user_by_id(self, id: str) -> UserData:
        # NOTE: ID could be a uuid
        ...

    @abstractmethod
    async def add_user(self, user: UserData) -> None:
        ...