from internal.adapters.user_postgres_repository import PostgresUserRepository

from typing import TYPE_CHECKING
from sqlalchemy import create_engine

if TYPE_CHECKING: 
    from .commands import CreateUserHandler
    from sqlalchemy import Engine, Connection


class Commands: 
    def __init__(self, create_user_handler: "CreateUserHandler"): # other handlers
        self.create_user = create_user_handler


class Queries:
    def __init__(self):
        pass


class Application:
    def __init__(self, commands: Commands, queries: Queries):
        self.queries =  queries
        self.commands = commands


# NOTE: This should be moved out from the application.
# And pass the config here as well which contains all env variables 
def create_application() -> Application:
    sql_engine: Engine = create_engine()
    postgres_conn: Connection = sql_engine.connect()

    user_repo = PostgresUserRepository(postgres_conn) 

    commands = Commands(CreateUserHandler(user_repo))

    queries = Queries()

    return Application(commands, queries)