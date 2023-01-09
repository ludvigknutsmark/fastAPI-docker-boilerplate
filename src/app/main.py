from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Own imports
from . import crud, models, schemas
from .database import SessionLocal, engine

# create db tables
models.Base.metadata.create_all(bind=engine)

# Lock. Unique DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello from FastAPI boilerplate"}

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No user")
    return user

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    print(user)
    return crud.create_user(db=db, user=user)