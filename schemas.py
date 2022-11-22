from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')
class CarsSchema(BaseModel):
    id: Optional[int]=None
    brand: Optional[str]=None
    model: Optional[str]=None
    price: Optional[str] = None

    class Config:
        orm_mode = True

class RequestCars(BaseModel):
    parameter = CarsSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]