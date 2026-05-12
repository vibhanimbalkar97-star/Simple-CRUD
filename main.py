from fastapi import FastAPI
from routes.TodoRoute import router as TodoRouter

app = FastAPI()

app.include_router(TodoRouter)

