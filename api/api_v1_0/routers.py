from fastapi import APIRouter

from api.api_v1_0.endpoints.register import router as register_router

router = APIRouter()

router.include_router(register_router)
