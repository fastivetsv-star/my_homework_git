from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

# 1. Створюємо додаток
app = FastAPI()

# 2. Підключаємо папку зі статикою (CSS, картинки)
# У Flask це було автоматично, у FastAPI треба явно сказати "змонтуй папку static"
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. Налаштовуємо шаблони (твої HTML файли)
templates = Jinja2Templates(directory="templates")

# 4. Створюємо Pydantic-модель для фільму (Валідація даних!)
# Це те, чого не було у Flask. Тепер ми точно знаємо, що рейтинг - це число.
class Film(BaseModel):
    title: str
    author: str
    rating: float
# Додаємо список книг
books_data = [
    {"title": "Гаррі Поттер", "author": "Дж. К. Роулінг"},
    {"title": "Володар Перснів", "author": "Дж. Р. Р. Толкін"},
    {"title": "Кобзар", "author": "Тарас Шевченко"}
]
# Наші дані (тепер це список об'єктів Film, а не просто словників)
library1 = [
    Film(title="Людина Паук", author="Стен Ли", rating=8),
    Film(title="Прокляття Аннабель", author="Гари Доберман", rating=9),
    Film(title="Дюна", author="Джеймс Ван", rating=7)
]

# --- Маршрути (Routes) ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # У FastAPI обов'язково треба передавати 'request' у шаблон!
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/films", response_class=HTMLResponse)
async def films_list(request: Request):
    # Передаємо список фільмів у шаблон, як і раніше
    return templates.TemplateResponse("films.html", {"request": request, "films": library1})

@app.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    # Тут поки повернемо простий HTML через шаблон, якщо він є, 
    # або можна повернути текст, але краще створити contacts.html
    return """
    <h1>Контакти</h1>
    <p>Email: fastivetsv@gmail.com</p>
    <a href="/">Назад</a>
    """
@app.get("/books", response_class=HTMLResponse)
async def books_list(request: Request):
    # Повертаємо шаблон books.html і передаємо туди список книг
    return templates.TemplateResponse("books.html", {"request": request, "books": books_data})

# --- API Маршрут (Бонус!) ---
# Спробуй зайти на /api/films - ти отримаєш чистий JSON. 
# Це і є сила FastAPI: один код працює і для сайту, і для мобільного додатка.
@app.get("/api/films", response_model=List[Film])
async def get_films_json():
    return library1