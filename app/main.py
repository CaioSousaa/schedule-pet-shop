from fastapi import FastAPI
from app.routes.PetRoutes import router as pet_routes
from app.routes.ClientRoutes import router as client_routes
from app.routes.ScheduleRoutes import router as schedule_routes
from app.routes.ZipRoutes import router as zip_routes

app = FastAPI()


app.include_router(pet_routes, prefix="/api", tags=["Pets"])

app.include_router(client_routes, prefix="/api", tags=["Clients"])

app.include_router(schedule_routes, prefix="/api", tags=["Schedules"])

app.include_router(zip_routes, prefix="/api", tags=["Zip"])