from pydantic import BaseModel
from typing import Optional

class Toys(BaseModel):
    id: Optional[int] = None
    title: str
    code: int
    category: str
    price: float  # Cambiado a float para representar un precio decimal
    stock: int
    description: str  # Corregido el nombre de la variable
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Toys title",
                "code": 123,  # Cambiado a un número entero
                "category": "Toy category",
                "price": 10.99,  # Cambiado a un ejemplo de precio en punto flotante
                "stock": 100,
                "description": "Well description"
            }
        }