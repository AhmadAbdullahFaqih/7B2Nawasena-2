from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CarsSchema, RequestCars, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

@router.post('/create')
async def create(request:RequestCars, db: Session=Depends(get_db())):
    crud.create_car(db, car=request.parameter)
    return Response(code=200, status='ok', message='Book Created Successfully').dict(exclude_none=True)

@router.get('/')
async def get(db:Session=Depends(get_db())):
    _car = crud.get_car(db,0,100)
    return Response(code=200, status='Ok', message='Success fetch all data', result=_car).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id:int, db: Session = Depends(get_db())):
    _car = crud.get_car_by_id(db,id)
    return Response(code=200, status='Ok', message='Success get data', result=_car).dict(exclude_none=True)

@router.post('/update')
async def update_book(request:RequestCars, db:Session=Depends(get_db())):
    _car = crud.update_car(db, car_id=request.parameter.id, title=request.parameter.title,
                             description=request.parameter.description)
    return Response(code=200, status='Ok', message='success update data', result=_car)

@router.delete('/{id}')
async def delete(id: int, db: Session=Depends(get_db())):
    crud.remove_car(db, car_id=id)
    return Response(code=200, status='ok', message='success delete data').dict(exclude_none=True)