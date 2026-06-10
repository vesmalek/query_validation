from fastapi import FastAPI, Query
from typing import Literal, Annotated
from pydantic import BaseModel, Field

app = FastAPI()

items = ["FastAPI tutorial", "Python basics", "Django REST", "FastAPI with databases", "React frontend"]

products = [
    {"name": "shirt", "price": 29.99, "in_stock": True},
    {"name": "shoes", "price": 59.99, "in_stock": False},
    {"name": "hat", "price": 14.99, "in_stock": True},
    {"name": "belt", "price": 9.99, "in_stock": True},
    {"name": "socks", "price": 4.99, "in_stock": False},
]

class SearchParams(BaseModel):
    model_config = {"extra", "forbid"}

    q: str = Field(min_length=2, max_length=100, alias='search-keyword')
    skip: int = Field(0, ge=0)
    limit: int = Field(10, ge=1, le=100)
    exact_match: bool = False

class ProductFilters(BaseModel):
    model_config = {"extra", "forbid"}

    skip: int = Field(0, ge=0)
    limit: int = Field(10, ge=1, le=50)
    sort_by: Literal['name', 'price'] = 'name'
    in_stock: bool | None = None


@app.get("/products")
async def get_products(filters: Annotated[ProductFilters, Query()]):
    results = products

    results = sorted(results, key=lambda d: d[filters.sort_by])

    if filters.in_stock is not None:
        results = [p for p in results if p['in_stock']== filters.in_stock]

    return results[filters.skip: filters.skip + filters.limit]

@app.get("/search")
async def search(filters: Annotated[SearchParams, Query()]):
    result = items

    if filters.exact_match:
        result = [p for p in result if p.lower().strip() == filters.q.lower().strip()]
    else:
        result = [p for p in result if filters.q.lower().strip() in p.lower().strip()]

    return result[filters.skip: filters.skip + filters.limit]
    
