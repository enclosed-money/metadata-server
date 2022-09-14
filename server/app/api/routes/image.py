from fastapi.responses import FileResponse
from fastapi import APIRouter
import pathlib

dir_path = pathlib.Path(__file__).parent.resolve()

router = APIRouter()


@router.get("/{token_id}")
async def get_image(token_id: str):
    img_path = '/server/app/test.png'
    return FileResponse(str(img_path))
