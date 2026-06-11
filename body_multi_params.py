from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, le=50)
    category: str = Field("General", min_length=3, max_length=20)

@app.put("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(ge=1)],
    q: Annotated[str | None, Query()] = None,
    product: Product | None = None
):
    results = {
        'product_id': product_id
    }

    if q:
        results['q'] = q

    if product:
        results['product'] = product.model_dump()

    return results