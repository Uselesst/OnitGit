from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
from .health import router as health_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(health_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "ORM работает"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()