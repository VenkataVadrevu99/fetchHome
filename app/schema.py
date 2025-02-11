from pydantic import BaseModel


class ItemSchema(BaseModel):
    shortDescription: str
    price: str

class ReceiptSchema(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[ItemSchema]
    total: str