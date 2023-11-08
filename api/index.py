from fastapi import FastAPI
from api.utils.page import get_image


app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


@app.get("/read/{year}/{month}/{day}/{page}")
async def read_comic(year: int, month: int, day: int, page: int):
    return get_image(page=page, year=year, month=month, day=day)