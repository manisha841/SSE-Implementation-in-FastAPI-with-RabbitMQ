from pydantic import BaseModel

class BlogPayload(BaseModel):
    title:str
    content:str
    author:str
    comments:str