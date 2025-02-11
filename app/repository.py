from app.model import Receipt
from uuid import UUID, uuid4

_receipts_repo = {}

def save_receipt(receipt: Receipt):
    receipt_id = uuid4()
    _receipts_repo[receipt_id] = receipt
    return receipt_id


def get_receipt(receipt_id: UUID):
    try:
        return _receipts_repo[receipt_id]
    except KeyError:
        return None