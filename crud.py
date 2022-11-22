from sqlalchemy.orm import Session
from model import Cars
from schemas import CarsSchema

def get_car(db:Session, skip: int=0, limit:int=100):
    return db.query(Cars).offset(skip).limit(limit).all()

def get_car_by_id(db:Session, car_id: int):
    return db.query(Cars).filter(Cars.id == car_id).first()

def create_car(db:Session, Cars: CarsSchema):
    _car = Cars(title=Cars.title, description = Cars.description)
    db.add(_car)
    db.commit()
    db.refresh(_car)
    return _car

def remove_car(db:Session, car_id:int):
    _car = get_car_by_id(db=db, car_id=car_id)
    db.delete(_car)
    db.commit()

def update_car(db:Session, car_id:int, title:str, description: str):
    _car = get_car_by_id(db=db, car_id=car_id)
    _car.title = title
    _car.description = description
    db.commit()
    db.refresh(_car)
    return _car