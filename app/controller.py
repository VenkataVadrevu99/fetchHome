from fastapi import APIRouter, HTTPException
from uuid import UUID

from app.mapper import map_to_receipt
from app.schema import ReceiptSchema
from app import service

receipts = APIRouter(prefix="/receipts", tags=["receipts"])

@receipts.get("/{receipt_id}/points")
async def get_receipts(receipt_id: str):
    try:
        uuid = UUID(receipt_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid receipt ID")
    return service.get_receipt(uuid)

@receipts.post("/process")
async def process_receipt(data: ReceiptSchema):
    receipt = map_to_receipt(data)
    return service.save_receipt(receipt)
