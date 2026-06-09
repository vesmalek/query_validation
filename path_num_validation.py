from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

products = ["shirt", "shoes", "hat", "belt", "socks", "watch", "bag", "jacket", "scarf", "gloves"]

@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(
        title='Product ID',
        description='Return product with the specified ID',
        ge=1
    )]
):
    return {'product_id': product_id}

@app.get("/products")
async def get_products(
    skip: Annotated[int, Query(
        ge=0
    )] = 0,
    limit: Annotated[int, Query(
        ge=1,
        le=50
    )] = 10
):
    return products[skip: skip + limit]

@app.get('/items/{item_id}')
async def get_item(
    item_id: Annotated[int, Path(
        title='Item ID',
        gt=0,
        le=9999
    )],
    price_min: Annotated[float | None, Query(
        ge=0.0
    )] = 0.0,
    price_max: Annotated[float | None, Query(
        gt=0.0
    )] = None
):
    return {
        'item_id': item_id,
        'price_min': price_min,
        'price_max': price_max
    }