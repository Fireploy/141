from sqlalchemy.orm import Session
from models.user import User

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user