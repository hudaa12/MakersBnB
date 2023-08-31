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
            'SELECT spaces.id AS space_id, spaces.name AS space_name, spaces.user_id, spaces.price, ' \
            'FROM users JOIN spaces ON users.id = spaces.user_id WHERE users.id = %s', [user_id])
        spaces = []
        for row in rows:
            spaces.append(Space(row['space_id'], row['space_name'], row['description'], row['price']))
        
        rows = self._connection.execute(
            'SELECT bookings.id AS booking_id, bookings.booking_date, bookings.booked_by, bookings.space_id, ' \
            'FROM users JOIN bookings ON users.id = bookings.booked_by WHERE users.id = %s', [user_id])
        bookings = []
        for row in rows:
            bookings.append(Booking(row['space_id'], row['space_name'], row['description'], row['price']))
        
        return User(row['id'], row['cohort_name'], row['starting_date'], spaces, bookings)

    def create(self, user):
        rows = self._connection.execute( 'INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id', 
        [user.email, user.password]
        )
        user.id = rows[0]['id']

    def check_user_login(self, email, password):
        row = self._connection.execute('SELECT * from users where email = %s AND password = %s', [email, password])
        if len(row) == 0:
            return None
        else:
            return row[0]['id']

