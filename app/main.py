from fastapi import FastAPI, responses

from app.controller import receipts

app = FastAPI()
app.include_router(receipts)

@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse(url="/docs")
