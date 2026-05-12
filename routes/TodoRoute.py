from fastapi import APIRouter
from models.TodoModel import Todo
router = APIRouter(prefix="/api/v1")

todos = []

# post
@router.post("/create")
def createTodo(data:Todo):
    new_data = dict(data)
    new_data['id'] = len(todos) + 1
    todos.append(new_data)
    return data

# get all todos
@router.get("/")
def get():
    return todos

# get todos by id
@router.get("/{id}")
def getById(id: int):
    for todo in todos:
        if todo['id'] == id:
            return todo