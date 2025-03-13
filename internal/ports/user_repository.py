from ..domain.user import UserData

from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    async def get_user_by_email(self):
        pass