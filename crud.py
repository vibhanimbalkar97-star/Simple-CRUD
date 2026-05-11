from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

fruits = [
  {
    "id": 1,
    "name": "Apple",
    "color": "Red",
  },
  {
    "id": 2,
    "name": "Mango",
    "color": "Yellow",
  },
  {
    "id": 3,
    "name": "Blueberry",
    "color": "Blue", 
  }
]

app = FastAPI()

# get all items
@app.get("/fruits")
def get_fruits():
    return fruits

# get fruits by id
@app.get("/fruits/{fruit_id}")
def get_fruit(fruit_id:int):
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            return fruit
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fruit not foud")  

# post 
class Fruit(BaseModel):  
    id:int
    name:str
    color:str

@app.post("/fruits")
def create_fruit(fruit: Fruit):
    new_fruit =fruit.model_dump()
    fruits.append(new_fruit)
    return fruit

# put
class updateFruit(BaseModel):
    name:str
    color:str

@app.put("/fruits/{fruit_id}")
def update_fruit(fruit_id:int, update_fruit:updateFruit):
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            fruit["name"] = update_fruit.name
            fruit["color"] = update_fruit.color
            return fruit
    raise HTTPException(status_code =  status.HTTP_404_NOT_FOUND, detail="Fruit not found")
    
# delete
@app.delete("/fruits/{fruit_id}")
def delete(fruit_id:int):
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            fruits.remove(fruit)
            return {"message": "Deleted"}
    raise HTTPException(status_code =  status.HTTP_404_NOT_FOUND, detail="Fruit not found")
    