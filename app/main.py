from fastapi import FastAPI
from app.routes.PetRoutes import router as pet_routes

app = FastAPI()


app.include_router(pet_routes, prefix="/api")


@app.get("/")
def hello_world():
    return {"msg": "hello world"}
