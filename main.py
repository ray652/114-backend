from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None=None
    price: float
    tax: float |None=None



app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

fake_items_db= [
    {"items_name" :"Foo"},
    {"items_name" :"Bar"},
    {"items_name" :"Baz"}
]
    
@app.post("/items/")
async def create_item(item:Item):
    item_dict = item.model_dump()  #item_dict()
    if item.tax is not None:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def ipdate_item(item_id:int,item:Item,q:str |None=None):
    result={"item_id":item_id,**item.model_dump()}
    if q:
        result.update({"q":q})
    return result

