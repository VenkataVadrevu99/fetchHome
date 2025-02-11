from decimal import Decimal
from datetime import datetime, time
from uuid import uuid4, UUID

from pydantic import BaseModel


class Item(BaseModel):
    shortDescription: str
    price: Decimal


class Receipt(BaseModel):
    retailer: str
    purchaseDate: datetime
    purchaseTime: time
    items: list[Item]
    total: Decimal