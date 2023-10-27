import uvicorn

from queries import create_blog_async_edgeql
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import edgedb

app = FastAPI()


from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


EDGEDB_HOST=os.getenv('EDGEDB_HOST')
EDGEDB_PORT=os.getenv('EDGEDB_PORT')
EDGEDB_USER=os.getenv('EDGEDB_USER')
EDGEDB_PASSWORD=os.getenv('EDGEDB_PASSWORD')
EDGEDB_DB=os.getenv('EDGEDB_DB')
EDGEDB_TLS_CA=os.getenv('EDGEDB_TLS_CA')


class BlogPayload(BaseModel):
    title:str
    content:str
    author:str
    comments:str


@app.post("/blog")
async def create_blog(payload:BlogPayload):
    try:
        new_item = payload
        print("New item to be added is ", new_item.__dict__)
        con = edgedb.create_async_client(
        host=EDGEDB_HOST,
        port=EDGEDB_PORT,
        user=EDGEDB_USER,
        password=EDGEDB_PASSWORD,
        database=EDGEDB_DB,
        tls_ca=EDGEDB_TLS_CA,
        tls_security="default",
    )
        print(f'con is {con}')
        blog_obj = create_blog_async_edgeql.create_blog(
            con=con,
            title=new_item.title,
            content=new_item.content,
            author=new_item.author,
            comments=new_item.comments,
        )
        print(f'blog is {blog_obj}')
        if not blog_obj:
            raise Exception("Failed to insert the data into database.")
        return {"message": "Data inserted successfully.", "data" : blog_obj}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error inserting data into database.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)