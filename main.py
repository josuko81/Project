from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.toys import toy_router
from routers.user import user_router

app = FastAPI()
app.title = "Prueba 2"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(toy_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


toys = [
    {
    "id": 1,
    "title": "Muñeca",
    "code": 12345,
    "category": "Juguetes para niñas",
    "price": 15.99,
    "stock": 100,
    "description": "Muñeca de plástico con vestido",
    },
    {
    "id": 2,
    "title": "Auto a control remoto",
    "code": 67890,
    "category": "Juguetes para niños",
    "price": 24.99,
    "stock": 75,
    "description": "Auto a control remoto con luces y sonidos", 
    },
    {
    "id": 3,
    "title": "Puzzle de 100 piezas",
    "code": 54321,
    "category": "Juguetes educativos",
    "price": 9.99,
    "stock": 120,
    "description": "Puzzle con ilustraciones coloridas",        
    }
]
@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Hellos World</h1>")

@app.get("/", tags=["another"])
def message():
    return HTMLResponse("<h1>Hellos World</h1>")
