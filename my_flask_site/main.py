from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


class Film(BaseModel):
    title: str
    author: str
    rating: float

books_data = [
    {"title": "Гаррі Поттер", "author": "Дж. К. Роулінг"},
    {"title": "Володар Перснів", "author": "Дж. Р. Р. Толкін"},
    {"title": "Кобзар", "author": "Тарас Шевченко"}
]

library1 = [
    Film(title="Людина Паук", author="Стен Ли", rating=8),
    Film(title="Прокляття Аннабель", author="Гари Доберман", rating=9),
    Film(title="Дюна", author="Джеймс Ван", rating=7)
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
  
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/films", response_class=HTMLResponse)
async def films_list(request: Request):
 
    return templates.TemplateResponse("films.html", {"request": request, "films": library1})

@app.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    
    return """
    <h1>Контакти</h1>
    <p>Email: fastivetsv@gmail.com</p>
    <a href="/">Назад</a>
    """
@app.get("/books", response_class=HTMLResponse)
async def books_list(request: Request):
    
    return templates.TemplateResponse("books.html", {"request": request, "books": books_data})


@app.get("/api/films", response_model=List[Film])
async def get_films_json():
    return library1