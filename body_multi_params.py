from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# task 02, 03, 04 and 05 pending. Complete these as well from 'Body - Multiple Parameters'

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

# Task 2
# Create POST /orders with two body models:
# - order: OrderItem (product_name: str, quantity: int, price: float)
# - customer: Customer (name: str, email: str)
# Return both combined in one dict
# Test in /docs — notice the JSON requires both wrapped under their names
# Test in test.py:
# requests.post("/orders", json={
#     "order": {"product_name": "shirt", "quantity": 2, "price": 29.99},
#     "customer": {"name": "Ismail", "email": "ismail@mail.com"}
# })

# Task 3
# Create POST /shipments with:
# - product: Product (from Task 1)
# - priority: Annotated[int, Body(ge=1, le=5)]
# - notes: Annotated[str | None, Body()] = None
# Return all three
# The body should look like:
# {
#     "product": {"name": "...", "price": ..., "category": "..."},
#     "priority": 3,
#     "notes": "Handle with care"
# }

# Task 4
# Create POST /products using embed=True:
# - product: Annotated[Product, Body(embed=True)]
# Test that FastAPI expects:
# {"product": {"name": "shirt", "price": 29.99, "category": "clothing"}}
# NOT:
# {"name": "shirt", "price": 29.99, "category": "clothing"}
# Open /docs and observe how the schema differs from a normal body endpoint

# Task 5 — Full combination
# Create POST /users/{user_id}/checkout with:
# - user_id: Annotated[int, Path(ge=1)]
# - coupon: Annotated[str | None, Query(min_length=4, max_length=20)] = None
# - cart: CartItems model (items: list[str], total: float = Field(gt=0))
# - delivery: DeliveryInfo model (address: str, city: str, express: bool = False)
# - tip: Annotated[float, Body(ge=0)] = 0.0
# Return everything combined including a "final_total" computed as:
# cart.total + tip - (cart.total * 0.1 if coupon else 0)
# Test in /docs with a full request