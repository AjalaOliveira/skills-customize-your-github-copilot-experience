from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple Items API")


class ItemCreate(BaseModel):
    name: str
    price: float


class Item(ItemCreate):
    id: int


# In-memory storage for starter project
_items: List[Item] = [Item(id=1, name="Notebook", price=12.5)]
_next_id = 2


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.dict())
    _items.append(item)
    _next_id += 1
    return item
