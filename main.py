import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import edgedb
from dotenv import load_dotenv
import os

from queries import create_blog_async_edgeql

load_dotenv()

app = FastAPI()

EDGEDB_HOST = os.getenv('EDGEDB_HOST')
EDGEDB_PORT = os.getenv('EDGEDB_PORT')
EDGEDB_USER = os.getenv('EDGEDB_USER')
EDGEDB_PASSWORD = os.getenv('EDGEDB_PASSWORD')
EDGEDB_DB = os.getenv('EDGEDB_DB')
EDGEDB_TLS_CA = os.getenv('EDGEDB_TLS_CA')

class BlogPayload(BaseModel):
    title: str
    content: str
    author: str
    comments: str

@app.post("/blog")
async def create_blog(payload: BlogPayload):
    try:
        new_item = payload
        con = edgedb.create_async_client(
            host=EDGEDB_HOST,
            port=EDGEDB_PORT,
            user=EDGEDB_USER,
            password=EDGEDB_PASSWORD,
            database=EDGEDB_DB,
            tls_ca=EDGEDB_TLS_CA,
            tls_security="default",
        )
        blog_obj = await create_blog_async_edgeql.create_blog(
            con,
            title=new_item.title,
            content=new_item.content,
            author=new_item.author,
            comments=new_item.comments,
        )
        if not blog_obj:
            raise HTTPException(status_code=400, detail="Failed to insert data into the database.")
        return {"message": "Data inserted successfully.", "data": blog_obj}
    except Exception as e:
        # Log the error and provide a more informative error message
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
