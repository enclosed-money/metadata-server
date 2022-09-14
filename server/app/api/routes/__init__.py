from fastapi import APIRouter
from app.api.routes.token import router as token_router
from app.api.routes.image import router as image_router

router = APIRouter()
router.include_router(token_router, prefix="/token", tags=["token"])
router.include_router(image_router, prefix="/image", tags=["image"])