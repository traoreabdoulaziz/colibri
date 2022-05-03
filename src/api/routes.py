from fastapi import APIRouter
from .controller  import user,file_controller

router = APIRouter()
router.include_router(user.user_router)
router.include_router(file_controller.router)


