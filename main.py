from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port=8080, reload=True)
