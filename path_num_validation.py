from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(
        title='Product ID',
        description='Return product with the specified ID',
        ge=1
    )]
):
    return {'product_id': product_id}