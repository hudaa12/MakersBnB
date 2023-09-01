from lib.space import Space
class SpaceRepository:
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces =[]
        for row in rows:
            space = Space(row['id'], row['name'], row['description'], row['price'], row['avail_from'], row['avail_to'], row['profile_photo'], row['user_id'])
            spaces.append(space)
        return spaces
    
    def find(self,id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row['id'], row['name'], row['description'], row['price'], row['avail_from'], row['avail_to'], row['profile_photo'], row['user_id'])

    
    def create(self,space):
        self._connection.execute('INSERT INTO spaces (name, description, price, avail_from, avail_to, profile_photo, user_id) VALUES (%s,%s,%s,%s,%s,%s,%s)', [space.name, space.description, space.price, space.avail_from, space.avail_to, space.profile_photo, space.user_id])
        return None
    
    # def delete(self,House_1):
    #     self._connection.execute('DELETE FROM spaces WHERE name = %s',[self.name])
    #     return None