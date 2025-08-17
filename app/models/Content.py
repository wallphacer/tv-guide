class Content:
    def __init__(self, id: int, title: str, type: str, runtime_minutes: int, episodes: int, seasons: int, poster: str, release_date: str):
        self.id = id
        self.type = type
        self.title = title
        self.runtime_minutes = runtime_minutes
        self.episodes = episodes
        self.seasons = seasons
        self.poster = poster
        self.release_date = release_date

class Channel:
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

class Showing:
    def __init__(self, id: int, channel: Channel, content: Content, time: int):
        self.id = id
        self.channel = channel
        self.content = content
        self.time = time


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class LikedContent:
    def __init__(self, id: int, user: User, content: Content, season: int, episode: int):
        self.id = id
        self.user = user
        self.content = content
        self.season = season
        self.episode = episode