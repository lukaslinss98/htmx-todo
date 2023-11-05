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

create_db()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
	todos = DB.get_todos()
	return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/api/createTodo", response_class=HTMLResponse)
async def createTodo(request: Request, text_input: Annotated[str, Form()]):
	id = DB.insert_todo(text_input)
	return templates.TemplateResponse("todo.html", {"request": request, "text_input": text_input,"status": "In Progress" ,"id" : id})

@app.delete("/api/deleteTodo", response_class=HTMLResponse)
async def deleteTodo(request: Request, id: int):
	DB.delete_todo(id)
	return HTMLResponse("")	

@app.delete("/api/deleteAll", response_class=HTMLResponse)
async def deleteTodo(request: Request):
	DB.delete_all()
	return HTMLResponse("")	


@app.put("/api/updateStatus", response_class=HTMLResponse)
async def deleteTodo(request: Request, id: int):
	(id, text_input, status) = DB.update_todo(id)
	return templates.TemplateResponse("todo.html", {"request": request, "text_input": text_input, "status": status ,"id" : id})
