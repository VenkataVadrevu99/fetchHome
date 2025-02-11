import math
from fastapi import HTTPException
from datetime import time
from decimal import Decimal
from uuid import UUID
from app.model import Receipt
from app import repository


def _calculate_points(receipt: Receipt) -> int:
    points = 0

    # 1. One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt.retailer)

    # 2. 50 points if the total is a round dollar amount (no cents)
    if receipt.total % 1 == 0:
        points += 50

    # 3. 25 points if the total is a multiple of 0.25
    if receipt.total % Decimal("0.25") == 0:
        points += 25

    # 4. 5 points for every two items on the receipt
    points += (len(receipt.items) // 2) * 5

    # 5. If item description length is a multiple of 3, apply price-based points
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += math.ceil(item.price * Decimal("0.2"))

    # 6. 5 points if the total is greater than 10.00 (and if using an LLM)
    # if receipt.total > Decimal("10.00"):
    #     points += 5

    # 7. 6 points if the purchase date day is odd
    if receipt.purchaseDate.day % 2 == 1:
        points += 6

    # 8. 10 points if the purchase time is after 2:00 PM and before 4:00 PM
    if time(14, 0) <= receipt.purchaseTime < time(16, 0):
        points += 10

    return points

def save_receipt(receipt: Receipt):
    receipt_id = repository.save_receipt(receipt)
    return {"id": receipt_id }

def get_receipt(receipt_id: UUID) -> int:
    receipt = repository.get_receipt(receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return _calculate_points(receipt)
