from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing_extensions import Annotated  
from models.Todo import Todo
from init import create_db
import DB

app = FastAPI()

#create_db()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
	todos = DB.get_todos()
	return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/api/createTodo", response_class=HTMLResponse)
async def createTodo(request: Request, text_input: Annotated[str, Form()]):
	DB.insert_todo(text_input)
	return templates.TemplateResponse("todo.html", {"request": request, "text_input": text_input})