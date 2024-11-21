from fastapi import FastAPI
from app.routes.PetRoutes import router as pet_routes
from app.routes.ClientRoutes import router as client_routes
from app.routes.ScheduleRoutes import router as schedule_routes

app = FastAPI()


app.include_router(pet_routes, prefix="/api", tags=["Pets"])

app.include_router(client_routes, prefix="/api", tags=["Clients"])

app.include_router(schedule_routes, prefix="/api", tags=["Schedules"])