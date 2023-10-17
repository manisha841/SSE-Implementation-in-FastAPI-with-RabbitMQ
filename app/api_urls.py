from fastapi import APIRouter

from src.blog.entrypoints import blog_endpoint

routes = APIRouter()

routes.include_router(blog_endpoint.router, tags=["Blog App"])
