from fastapi import FastAPI
from api.utils.page import get_image
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


@app.get("/read/{year}/{month}/{day}/{page}")
async def read_comic(year: int, month: int, day: int, page: int):
    return get_image(page=page, year=year, month=month, day=day)
