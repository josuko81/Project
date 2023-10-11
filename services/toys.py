from models.toys import Toyss as ToyModel
from schemas.toys import Toys

class ToysService():

    def __init__(self, db) -> None:
        self.db = db
        
    def get_toys(self):
        result = self.db.query(ToyModel).all()
        return result
    def get_toy(self, id):
        result = self.db.query(ToyModel).filter(ToyModel.id == id).first()
        return result
    def get_toys_by_category(self, category):
        result = self.db.query(ToyModel).filter(ToyModel.category == category).all()
        return result
    def create_movie(self, toy: Toys):
        new_toy = ToyModel(**toy.dict())
        self.db.add(new_toy)
        self.db.commit()
        return
    def update_toy(self, id: int, data: Toys):
        toy = self.db.query(ToyModel).filter(ToyModel.id == id).first()
        toy.title = data.title
        toy.code = data.code
        toy.category = data.category
        toy.price = data.price
        toy.stock = data.stock
        toy.description = data.description
        self.db.commit()
        return
    def delete_movie(self, id: int):
        self.db.query(ToyModel).filter(ToyModel.id == id).delete()
        self.db.commit()
        return