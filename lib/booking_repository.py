from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_booking(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (booking_date, booked_by, space_id) VALUES (%s, %s, %s, %s) RETURNING id', [booking.booking_date, booking.booked_by, booking.space_id])
        booking.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM bookings'
        )
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_date'],
                           row['confirmed'], row['booked_by'], row['space_id'])
            bookings.append(item)
        return bookings

    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s',
            [id]
        )
        row = rows[0]
        return Booking(row['id'], row['booking_date'], row['confirmed'], row['booked_by'], row['space_id'])

    def delete(self, id):
        self._connection.execute(
            'DELETE FROM bookings WHERE id = %s',
            [id]
        )
        return None
