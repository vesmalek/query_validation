from typing import Annotated
from fastapi import FastAPI, Query, Path

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

@app.get("/products")
async def get_products(
    skip: int = 0,
    limit: Annotated[int, Query()] = 10,
    category: Annotated[str | None, Query(
        min_length=2,
        max_length=30
    )] = None,
    sort: Annotated[str, Query(
        min_length=2,
        max_length=10
    )] = "name"
):
    return {
        "skip": skip,
        "limit": limit,
        "category": category,
        "sort": sort
    }

@app.get("/tags")
async def get_tags(
    tags: Annotated[list[str] | None, Query()] = None
):
    return {"tags": tags}

@app.get("/items")
async def get_items(
    category: Annotated[str, Query(
        alias='item-category',
        min_length=2
    )]
):
    return {'category': category}