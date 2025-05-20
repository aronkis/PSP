from Domain.IBookingRepository import IBookingRepository
from Repositories.Repository import Repository
from Domain.Booking import Booking
import json

class BookingRepository(IBookingRepository):
    def __init__ (self):
        self.__booking_repository: Repository = Repository()

    def CreateBooking(self, booking: Booking) -> None:
        if not isinstance(booking, Booking):
            raise ValueError("Expected a Booking object.")
        self.__booking_repository.ModifyData(""" INSERT INTO Booking (start_date, end_date, client_id, room_id) VALUES (?, ?, ?, ?) """, \
                       (booking.GetStartDate(), booking.GetEndDate(), booking.GetClientId(), booking.GetRoomId()))
    
    def ListBookings(self) -> dict:
        data:str = self.__booking_repository.GetData("SELECT * FROM Booking")
        return json.loads(data)
