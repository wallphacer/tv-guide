import json
from types import SimpleNamespace
from app.models.Content import Content


class Mapper(object):
    def __init__(self):
        return

    def map_content(self, data):
        ob = json.loads(data, object_hook=SimpleNamespace)
        return Content(1, ob.title, ob.type, 0, 1,1,ob.poster, ob.year)