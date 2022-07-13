import uvicorn
from fastapi import FastAPI

from api.api_v1_0.routers import router as api_router_v1_0

app = FastAPI()

app.include_router(api_router_v1_0, prefix='/api_v1.0')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
