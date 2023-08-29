from lib.booking import Booking
from lib.booking_repository import BookingRepository
from datetime import date

"""
When we call BookingRepository#all
We get a list of Booking objects reflecting the seed data
"""
def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = BookingRepository(db_connection)
    assert repository.all() == [
        Booking(1, date(2023,7,10), True, 3, 1),
        Booking(2, date(2023,8,15), True, 2, 2),
        Booking(3, date(2023,9,20), True, 1, 3)
    ]

'''
When we call BookingRepository#find
We get a single Booking object
'''
def test_get_single_booking(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = BookingRepository(db_connection)
    print(repository.find(1))
    assert repository.find(1) == Booking(1, date(2023,7,10), True, 3, 1)
