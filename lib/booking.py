class Booking:
    def __init__(self, id, booking_date, confirmed, booked_by, space_id):
        self.id = id
        self.booking_date = booking_date
        self.confirmed = confirmed
        self.booked_by = booked_by
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.booking_date}, {self.confirmed}, {self.booked_by}, {self.space_id})"