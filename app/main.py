from fastapi import FastAPI
from app.routes.PetRoutes import router as pet_routes
from app.routes.ClientRoutes import router as client_routes
from app.routes.ScheduleRoutes import router as schedule_routes
from app.routes.ServicesRoutes import router as services_routes
from app.routes.ZipRoutes import router as zip_routes
from app.routes.HashRoutes import router as hash_routes
from app.routes.CountEntitiesRoutes import router as count_entities_pet_csv

app = FastAPI()


app.include_router(pet_routes, prefix="/api", tags=["Pets"])

app.include_router(client_routes, prefix="/api", tags=["Clients"])

app.include_router(schedule_routes, prefix="/api", tags=["Schedules"])

app.include_router(services_routes, prefix="/api", tags=["Services"])

app.include_router(zip_routes, prefix="/api", tags=["Zip"])

app.include_router(hash_routes, prefix="/api", tags=["Hash"])

app.include_router(count_entities_pet_csv, prefix="/api", tags=["CountEntities"])
