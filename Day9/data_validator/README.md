Pydantic Data Validator -- Food Order
Pydantic BaseModel Field validator ValidationError
Real-world App
Swiggy / Zomato
Overview
Pydantic BaseModel with Field() constraints (ge, le, min_length, min_items). PaymentMethod uses 
Enum for restricted values. A custom @validator checks that order total > 0. ValidationError gives 
structured JSON error messages. This is exactly how FastAPI validates every request body -- 
mastering Pydantic means mastering FastAPI.
Problem
Food order validation using Pydantic. Structured error messages on invalid input. This is exactly 
how FastAPI validates request bodies.
Starter Code
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from enum import Enum
class PaymentMethod(str, Enum):
    UPI="upi"; CARD="card"; CASH="cash"
class OrderItem(BaseModel):
    name:     str   = Field(..., min_length=1, max_length=100)
    quantity: int   = Field(..., ge=1, le=20)
    price:    float = Field(..., gt=0)
class Order(BaseModel):
    customer_name:    str = Field(..., min_length=2)
    items:            List[OrderItem] = Field(..., min_items=1)
    delivery_address: str = Field(..., min_length=10)
    payment_method:   PaymentMethod
    tip:              Optional[float] = Field(None, ge=0, le=500)
    @validator("items")
    def total_must_be_positive(cls, items):
        if sum(i.price*i.quantity for i in items)<=0:
            raise ValueError("Order total must be > 0")
        return items
Constraints
•  Use Pydantic BaseModel -- not plain classes
•  All fields use Field() with constraints
•  Custom @validator for business rule