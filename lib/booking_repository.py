from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM bookings'
        )
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_date'], row['confirmed'], row['booked_by'], row['space_id'])
            bookings.append(item)
        return bookings
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT FROM bookings WHERE id = %s',
            [id]
        )
        row = rows[0]
        return Booking(row['id'], row['booking_date'], row['confirmed'], row['booked_by'], row['space_id'])