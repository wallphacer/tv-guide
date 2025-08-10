import fastapi
import uvicorn
import requests

from fastapi import FastAPI
API_KEY="[API-KEY]"

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/content/search")
def search_for_content(title :str, page: int = 1):
    response = requests.get("http://www.omdbapi.com/?apikey={API_KEY}&s={title}&page={page}".format(API_KEY=API_KEY, title=title, page=page))
    return response.json()

@app.get("/test/{item_id}")
def test(item_id: int):
    return {"item_id": item_id}

@app.post("/content/{content_id}")
def add_content_to_list(content_id: int):
    return {"content_id": content_id}

@app.delete("/content/{content_id}")
def delete_content(content_id: int):
    return {"content_id": content_id}