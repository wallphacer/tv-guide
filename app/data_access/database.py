import psycopg2
from app.models.Content import Content

class PostgresAccessor(object):

    def __init__(self, database_name: str, username: str, password: str, host:str, port:str):
        self.connection = psycopg2.connect(
            dbname=database_name,
            user=username,
            password=password,
            host=host,
            port=port
            )

    async def batch_add_content(self, data: dict):
        for entry in data:
            d = Content(1, entry['Title'], entry['Type'], 0, 1, 1, entry['Poster'], entry['Year'])
            await self.add_content(d)

    async def add_content(self, content: Content):
        query = """
                INSERT INTO "Media".content("Title", "Type", "Year", "Episodes", "Runtime_minutes", "Poster")
                VALUES (%s, %s, %s, %s, %s, %s);
                    
                COMMIT;
                """
        data = (content.title, content.type, content.release_date, content.episodes, content.runtime_minutes, content.poster)

        await self._execute(query, data)

    async def get_content(self, title: str):
        query = """
            SELECT * FROM "Media".content
            WHERE Title = %s;
        """
        data = (title,)
        results = self._execute(query, data)
        #TODO: Parse results

    async def _execute(self, query: str, data: tuple):
        with self.connection.cursor() as cursor:
            response = cursor.execute(query, data)
        return response