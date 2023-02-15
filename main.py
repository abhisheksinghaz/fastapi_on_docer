from typing import Union
import os
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess as sp

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/py")
def py_version():
    
    # output = sp.getoutput('whoami --version')
    # print (output)
    os.system("python --version")
    return {"v":"v"}
