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

    