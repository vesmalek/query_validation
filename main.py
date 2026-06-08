from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
async def search(
    q: Annotated[str | None, Query(
        title='Search query',
        description='Keyword to search products by name',
        min_length=2,
        max_length=100
    )] = None
):
    result = {"searching_for": q} if q else {"result": "no search term"}
    return result