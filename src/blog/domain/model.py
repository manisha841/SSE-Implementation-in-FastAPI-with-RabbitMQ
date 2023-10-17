
from uuid import UUID


class Blog:
    id:UUID
    title:str
    content:str
    author:str
    comment:str

async def create_blog_factory(
        title:str,
        content:str,
        author:str,
        comments:str,
) -> Blog:
    return Blog(
        title=title,
        content=content,
        author=author,
        comments=comments,
    )
    