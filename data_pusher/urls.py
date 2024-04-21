from data_pusher import controllers
from fastapi import APIRouter


router = APIRouter()
router.include_router(controllers.router)
