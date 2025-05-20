from Domain.Booking import Booking

class IBookingRepository:
    def CreateBooking(self, booking: Booking) -> None:
        pass

    def ListBookings(self) -> dict:
        pass