from ast import Store
from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name":"My Store",
        "items":[
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores":stores}

@app.post("/stores")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201

# To get the input parameter from url

@app.post("/stores/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            print("Yes cleared")
            new_item = {
                "name":request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404


# get data for a store
@app.get("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return store
    return {"message":"Store not found"}, 404

# get item data for a store
@app.get("/stores/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return {"items":store["items"]}
    return {"message":"Store not found"}, 404
