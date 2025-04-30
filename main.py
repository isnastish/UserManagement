from internal.domain.user import User

from fastapi import FastAPI

app = FastAPI()


users: list[User] = [
    User(username="Alexey", email="alexey@gmail.com", password="password89"),
    User(username="Fred", email="fred.b@gmail.com", password="unknowPass@")
]

@app.get("/users")
async def read_root() -> list[User]:
    return users 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port=8080, reload=True)
