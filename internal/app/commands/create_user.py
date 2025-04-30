from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from internal.ports.user_repository import UserRepository
    from internal.domain.user import User


# NOTE: We can even define an interface for the handler.

class CreateUserHandler:
    def __init__(self, user_repo: "UserRepository"):
        self._user_repo = user_repo

    async def handle(self, user: "User"):
        # TODO: Use try-except block
        await self._user_repo.add_user(user)