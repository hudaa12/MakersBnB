from lib.space import Space
class SpacesRepository:
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces =[]
        for row in rows:
            space = Space(row['name'],row['description'], row['price'], row['avail_from'], row['avail_to'], row['user_id'])
            spaces.append(space)
        return spaces