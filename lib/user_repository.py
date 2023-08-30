from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row["id"], row["email"], row["password"])
            users.append(user)
        return users

    def create(self, user):
        rows = self._connection.execute( 'INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id', 
        [user.email, user.password]
        )
        user.id = rows[0]['id']