from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/hi")
async def read_root(who: str = Body(embed=True)) -> dict[str, str]:
    return {"Hello": who}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port=8080, reload=True)
