from fastapi import FastAPI
from routes import user_controller
from config.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router)

@app.get("/")
def home():
    return {"message": "¡¡¡Fast api con Fireploy!!!"}
