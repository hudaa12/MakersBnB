from lib.booking import Booking

"""
When creating a booking object
Returns nothing
"""
def test_create_booking():
    booking = Booking(1, "10/03/2023", True, 1, 2)
    assert booking.id == 1
    assert booking.booking_date == "10/03/2023"
    assert booking.confirmed == True
    assert booking.booked_by == 1
    assert booking.space_id == 2

"""
Given two identical bookings
I can have them to be equal
"""
def test_bookings_equal():
    booking1 = Booking(1, "10/03/2023", True, 1, 2)
    booking2 = Booking(1, "10/03/2023", True, 1, 2)
    assert booking1 == booking2

"""
Format Booking object to string nicely
"""
def test_format_booking_nicely():
    booking = Booking(1, "10/03/2023", True, 1, 2)
    assert str(booking) == "Booking(1, 10/03/2023, True, 1, 2)"