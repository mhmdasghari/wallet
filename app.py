import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.api_v1_0.routers import router as api_router_v1_0

app = FastAPI()

app.mount("/statics", StaticFiles(directory="statics"), name="statics")

app.include_router(api_router_v1_0, prefix='/api_v1.0')

if __name__ == "__main__":
    uvicorn.run(app)
