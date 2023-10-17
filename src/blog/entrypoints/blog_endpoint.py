from uuid import UUID
from src.blog.service_layer import blog_service

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
    blog_obj = await blog_service.create_blog(
        title=blog_info.title,
        content=blog_info.content,
        author=blog_info.author,
        comments=blog_info.comments,
        con=con,
        )
    return blog_obj
    