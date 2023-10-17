from uuid import UUID

from fastapi import APIRouter, Depends, Request,status

from src.blog.schemas.schemas import BlogPayload

router = APIRouter()


@router.post("/blog/",status_code=status.HTTP_200_OK)
async def create_blog(
    *,
    request:Request,
    blog_info:BlogPayload,
):
    con = ''
    blog_obj = await 