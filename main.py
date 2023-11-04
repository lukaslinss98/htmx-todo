from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing_extensions import Annotated



class TodoRequest(BaseModel):
	content: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/createTodo", response_class=HTMLResponse)
async def createTodo(request: Request, text_input: Annotated[str, Form()]):

	return templates.TemplateResponse("todo.html", {"request": request, "text_input": text_input})