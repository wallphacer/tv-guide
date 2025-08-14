import fastapi
import uvicorn
import requests
from app.req.reqs import search
import json
from types import SimpleNamespace
from fastapi import FastAPI
from app.models.Content import Content
import psycopg2


API_KEY="[api_key]"

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/content/search")
def search_for_content(title :str, page: int = 1):
    resp =  search(API_KEY, title, page)
    print(resp)
    print(resp['Search'])
    print("--")
    print(resp.__class__.__name__)
    map_content(resp['Search'])
    return resp

@app.get("/test/{item_id}")
def test(item_id: int):
    return {"item_id": item_id}

@app.post("/content/{content_id}")
def add_content_to_list(content_id: int):
    return {"content_id": content_id}

@app.delete("/content/{content_id}")
def delete_content(content_id: int):
    return {"content_id": content_id}


def map_content(data):
    conn = psycopg2.connect(
        dbname="tvguide",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    # we use a context manager to scope the cursor session
    with conn.cursor() as curs:
        for entry in data:
            d = Content(1, entry['Title'], entry['Type'], 0, 1,1, entry['Poster'], entry['Year'])
            curs.execute(
                """
                INSERT INTO "Media".content("Title", "Type", "Year", "Episodes", "Runtime_minutes", "Poster")
                VALUES (%s, %s, %s, %s, %s, %s);
                    
                COMMIT;
                """,
                (d.title, d.type, d.release_date, d.episodes, d.runtime_minutes, d.poster)
            )
