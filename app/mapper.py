from decimal import Decimal
from datetime import datetime
from app.schema import ReceiptSchema
from app.model import Receipt, Item

def map_to_receipt(schema: ReceiptSchema) -> Receipt:
    return Receipt(
        retailer=schema.retailer,
        purchaseDate=datetime.strptime(schema.purchaseDate, "%Y-%m-%d"),
        purchaseTime=datetime.strptime(schema.purchaseTime, "%H:%M").time(),
        items=[
            Item(shortDescription=item.shortDescription, price=Decimal(item.price))
            for item in schema.items
        ],
        total=Decimal(schema.total)
    )
