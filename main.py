from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items", response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_name}", response_model=schemas.Item)
def get_items(item_name: str, db: Session = Depends(get_db)):
    items = crud.get_item(db, item_name=item_name)
    return items

@app.get("/items/temperature/{temp}", response_model=schemas.Item)
def get_items(temp: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items_by_temp(db, temp=temp, skip=skip, limit=limit)
    return items

@app.get("/items/category/{part}", response_model=schemas.Item)
def get_items(part: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items_by_bodypart(db, part=part, skip=skip, limit=limit)
    return items