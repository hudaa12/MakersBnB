from lib.user import User
from lib.space import Space
from lib.booking import Booking


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

    def find_with_spaces_and_bookings(self, user_id):
        rows = self._connection.execute(
            'SELECT users.id, users.email, users.password, '
            'spaces.id AS space_id, spaces.name AS space_name, spaces.description, spaces.price, '
            'spaces.avail_from, spaces.avail_to, spaces.user_id '
            'FROM users JOIN spaces ON users.id = spaces.user_id WHERE users.id = %s', [user_id])
        spaces = []
        for row in rows:
            spaces.append(Space(row['space_id'], row['space_name'], row['description'],
                          row['price'], row['avail_from'], row['avail_to'], row['user_id']))


        rows = self._connection.execute(
            'SELECT users.id, users.email, users.password, '
            'bookings.id AS booking_id, bookings.booking_date, bookings.booked_by, bookings.space_id '
            'FROM users JOIN bookings ON users.id = bookings.booked_by WHERE users.id = %s', [user_id])
        bookings = []
        for row in rows:
            bookings.append(Booking(row['booking_id'], row['booking_date'], row['booked_by'], row['space_id']))

        return User(row['id'], row['email'], row['password'], spaces, bookings)
        

    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id',
                                        [user.email, user.password]
                                        )
        user.id = rows[0]['id']

    def check_user_login(self, email, password):
        rows = self._connection.execute(
            'SELECT * from users where email = %s and password = %s', [email, password])
        if len(rows) == 0:
            return False
        else:
            return True

    def find_by_email(self, email):
        row = self._connection.execute(
            'SELECT * from users where email = %s', [email])
        return User(row[0]['id'], row[0]['email'], row[0]['password'])
