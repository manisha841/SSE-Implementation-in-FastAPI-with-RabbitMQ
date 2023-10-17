from src.blog.domain.model import Blog
from src.blog.service_layer import exceptions

from src.blog.service_layer.queries import create_blog_async_edgeql


class BlogRepository:
    def __init__(self, db: DbConnection):
        self.db = db

    async def create_blog(self,validated_data):
        return await create_blog_async_edgeql.create_blog(
            self.db,
            **validated_data.dict()
        )
        