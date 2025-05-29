from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal 
from services import user_service

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.post("/users")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return user_service.create_user(db, name, email)
