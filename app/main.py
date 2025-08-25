import fastapi
import uvicorn
import requests
import os
import configparser
from app.req.reqs import search
from fastapi import FastAPI
from app.data_access.database import PostgresAccessor

# DEPENDENCIES

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config/config.local.ini"))
database_connector = PostgresAccessor(database_name=config.get("postgres", "database_name"),
        username=config.get("postgres", "username"),
        password=config.get("postgres", "password"),
        host=config.get("postgres", "host"),
        port=config.get("postgres", "port"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

# CONTENT
@app.get("/content/search")
async def search_for_content(title :str, page: int = 1):
    #TODO: Search from the database after adding this content
    #TODO: Ensure content from omdb doesn't get added more than once
    resp =  search(config.get("omdb", "api_key"), title, page)
    print("Got Results!")
    await database_connector.batch_add_content(resp['Search'])

    return resp

@app.get("/liked/search/")
async def search_for_content(title :str):
    #TODO: Search from the database after adding this content
    #TODO: Ensure content from omdb doesn't get added more than once
    resp = await database_connector.get_content(title)
    print("Got Results!")
    print(resp)
    return resp


@app.post("/content/{content_id}")
def add_content_to_list(content_id: int):
    #TODO: Add Users
    #TODO: Create LikedContent table such that users can like & add content to LikedContent
    return {"content_id": content_id}

@app.get("/test/{item_id}")
def test(item_id: int):
    return {"item_id": item_id}

#TODO: This should be just deleting content from your LikedContent page
@app.delete("/content/{content_id}")
def delete_content(content_id: int):
    return {"content_id": content_id}
