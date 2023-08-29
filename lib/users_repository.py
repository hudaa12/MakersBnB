from lib.users import Users

class UsersRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = Users(row["id"], row["email"], row["password"])
            users.append(user)
        return users

    def new_user_created(self, user):
        self._connection.execute( 'INSERT INTO users (email, password) VALUES (%s, %s)', [
            user.email, user.password
        ])