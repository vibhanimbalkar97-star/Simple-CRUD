from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# intialize
app = FastAPI()

# models = define data structure
class Tea(BaseModel):
    id:int
    name:str
    origin:str

teas: List[Tea] = []


# FastAPI 
@app.get("/")
def read_root():
    return {"message": "Welcome"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_teas(tea_id:int, update_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_teas(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted= teas.pop(index)
            return deleted
    return {"error": "Not deleted"}

