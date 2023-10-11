from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.toys import Toyss as ToyModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.toys import ToysService
from schemas.toys import Toys

toy_router = APIRouter()

@toy_router.get("/toys", tags=["toys"], response_model=List[Toys], status_code=200, dependencies=[Depends(JWTBearer())])
def get_toys() -> Toys:
    db = Session()
    result = ToysService(db).get_toys()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
 
@toy_router.get("/toys/{id}", tags=["toys"], response_model=Toys)
def get_toy(id: int = Path(ge=1, le=2000)) -> Toys:
    db = Session()
    result =  ToysService(db).get_toy(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@toy_router.get("/toys", tags=["toys"], response_model=List[Toys])
def get_toys_by_category(category = str) -> List[Toys]:
    db = Session()
    result = ToysService(db).get_toys_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@toy_router.post("/toys", tags=["toys"], response_model=dict, status_code=201)
def create_toy(Toy: Toys) -> dict:
    db = Session()
    ToysService(db).create_toy(Toy)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

@toy_router.put("/toys{id}", tags=["toys"], response_model=dict, status_code=200)
def update_toy(id: int, Toy: Toys) -> dict:
    db = Session()
    result = ToysService(db).get_toy(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    ToysService(db).update_toy(id, Toy)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})

@toy_router.delete("/toys/{id}", tags=["toys"], response_model=dict, status_code=200)
def delete_toy(id: int) -> dict:
    db = Session()
    result: ToysService = db.query(ToyModel).filter(ToyModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    ToyModel(db).delete_toy(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})