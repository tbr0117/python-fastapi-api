from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import random

myApp = FastAPI()


class Item(BaseModel):
    Id: Optional[int]
    Name: str
    Price: float
    Is_offer: Optional[bool] = None


@myApp.get("/")
def read_root():
    return {"Hello": "Hey Dude", "Status": "You just takeoff with fastapi"}


@myApp.get("/Items/{item_id}")
def read_entity(item_id: int, q: Optional[str] = None):
    return {"ItemId": item_id, "Status": "You just takeoff with fastapi", "Query": q}


@myApp.post("/Items")
def create_entity(oItem: Item):
    return {"ItemId": random.randint(1, 100), "Name": oItem.Name, "Price": oItem.Price, "Status": "Okay, Will control further"}


@myApp.put("/Items/{ItemId}")
def create_entity(ItemId: int, oItem: Item):
    return {"ItemId": random.randint(), "Name": oItem.Name, "Price": oItem.Price, "Status": "Okay, Will control further"}
