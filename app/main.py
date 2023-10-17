import uvicorn
from fastapi import FastAPI, Request

from app.api_urls import routes


from fastapi import FastAPI  
app = FastAPI()   

@app.get("/") 
async def main_route():     
  return {"message": "Hello World"}

def add_routes(routes_urls, app: FastAPI):
    for route in routes_urls:
        app.include_router(route, 'localhost:8000')


if __name__ == "__main__":
    uvicorn.run(
        'app.main',
        host='localhost',
        port='8000',
        log_level="info",
    )
