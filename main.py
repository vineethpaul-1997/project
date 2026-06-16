from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
inventory = {"toys": 150, "apparel": 300}

class Item(BaseModel):
    category: str
    quantity: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Retail Inventory API"}

@app.get("/inventory/{category}")
def get_inventory(category: str):
    if category in inventory:
        return {"category": category, "stock": inventory[category]}
    return {"error": "Category not found"}

@app.get("/metrics")
def get_metrics():
    return {"status": "ok", "toys_stock": inventory["toys"], "apparel_stock": inventory["apparel"]}
