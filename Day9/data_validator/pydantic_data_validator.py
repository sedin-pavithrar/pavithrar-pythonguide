from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
from enum import Enum


class PaymentMethod(str, Enum):
    UPI = "upi"
    CARD = "card"
    CASH = "cash"


class OrderItem(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(..., ge=1, le=20)
    price: float = Field(..., gt=0)


class Order(BaseModel):
    customer_name: str = Field(..., min_length=2)
    items: List[OrderItem] = Field(..., min_items=1)
    delivery_address: str = Field(..., min_length=10)
    payment_method: PaymentMethod
    tip: Optional[float] = Field(None, ge=0, le=500)

    @field_validator("items")
    def total_must_be_positive(cls, items):
        total = sum(item.price * item.quantity for item in items)

        if total <= 0:
            raise ValueError("Order total must be > 0")

        return items


# --------------------------
# Valid Order
# --------------------------

try:
    order = Order(
        customer_name="Pavithra",
        items=[
            OrderItem(
                name="Pizza",
                quantity=2,
                price=250
            ),
            OrderItem(
                name="Burger",
                quantity=1,
                price=120
            )
        ],
        delivery_address="12 Anna Nagar, Chennai",
        payment_method="upi",
        tip=50
    )

    print("Order Created Successfully")
    print(order)

except ValidationError as e:
    print(e.json(indent=2))


# --------------------------
# Invalid Order
# --------------------------

try:
    invalid_order = Order(
        customer_name="P",          # too short
        items=[],                   # empty list
        delivery_address="Short",   # too short
        payment_method="bitcoin",   # invalid enum
        tip=-10                     # negative tip
    )

except ValidationError as e:
    print("\nValidation Errors:")
    print(e.json(indent=2))



