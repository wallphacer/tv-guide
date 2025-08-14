import requests


def search(api_key: str, search_by: str, page: int = 1):
    response = requests.get("http://www.omdbapi.com/?apikey={API_KEY}&s={title}&page={page}".format(API_KEY=api_key, title=search_by, page=page))
    return response.json()