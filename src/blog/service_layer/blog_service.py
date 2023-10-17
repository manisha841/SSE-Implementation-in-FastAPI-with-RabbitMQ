"""
"""
from __future__ import annotations

from uuid import UUID

from src.blog.schemas import schemas

from src.blog.domain import model


from src.blog.service_layer import  unit_of_work


async def create_blog(
    con: DbConnection,
    blog_schema: schemas.BlogPayload
):
    """Create blog with a required data information"""
    async with unit_of_work.BlogRepository(con) as uow:
        blog_obj = await model.create_blog_factory(
            title=blog_schema.title,
            content=blog_schema.content,
            author=blog_schema.author,
            comments=blog_schema.comments,
        )
        
        await uow.repository.create_blog(blog_obj)
        return blog_obj