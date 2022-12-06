from pydantic import BaseModel
from enum import IntEnum

class TemperatureEnum(IntEnum):
    cold = 0
    moderate = 1
    hot = 2

class CategoryEnum(IntEnum):
    hat = 0
    glasses = 1
    earring = 2
    scarf = 3
    coat = 4
    sweater = 5
    tshirt = 6
    gloves = 7
    pants = 8
    shorts = 9
    shoes = 10

class ItemBase(BaseModel):
    name: str
    price: float
    temperature: TemperatureEnum
    category: CategoryEnum
    image: str

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
