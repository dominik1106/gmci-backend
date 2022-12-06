from sqlalchemy.orm import Session

from . import models, schemas

def get_item(db : Session, item_name: str):
    return db.query(models.Item).filter(models.Item.name == item_name).first()

def get_items(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_items_by_temp(db : Session, temp: int, skip: int = 0, limit: int = 30):
    return db.query(models.Item).filter(models.Item.temperature == temp).offset(skip).limit(limit).all()

def get_items_by_bodypart(db : Session, part: int, skip: int = 0, limit: int = 30):
    return db.query(models.Item).filter(models.Item.category == part).offset(skip).limit(limit).all()