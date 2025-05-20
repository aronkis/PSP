from Services.IClientServices import IClientServices
from Repositories.RoomRepository import RoomRepository
from Repositories.BookingRepository import BookingRepository
from Domain.IRoomRepository import IRoomRepository
from Domain.IBookingRepository import IBookingRepository
from datetime import datetime
import json

class ClientServices(IClientServices):
    def __init__(self):
        self.__room_repository: IRoomRepository = RoomRepository()
        self.__booking_repository: IBookingRepository = BookingRepository()

    def ListAvailableRooms(self) -> str:
        rooms: json = self.__room_repository.ListRooms()
        bookings: json = self.__booking_repository.ListBookings()
        current_date = datetime.now().strftime("%Y-%m-%d")
        booked_room_ids = set()
        for row in bookings['rows']:
            start_date, end_date, room_id = row[1], row[2], row[3]
            if start_date <= current_date <= end_date:
                booked_room_ids.add(room_id)
        for room in rooms['rows'][:]:
            if room[0] in booked_room_ids:
                rooms['rows'].remove(room)
        data = json.dumps(rooms)
        return data

    def FilterRooms(self,
        location: str = None,
        price: float = None,
        position: str = None,
        facilities: str = None) -> str: 
        rooms:json = self.__room_repository.FilterRooms(location, price, position, facilities)
        bookings: json = self.__booking_repository.ListBookings()
        current_date = datetime.now().strftime("%Y-%m-%d")
        booked_room_ids = set()
        for row in bookings['rows']:
            start_date, end_date, room_id = row[1], row[2], row[3]
            if start_date <= current_date <= end_date:
                booked_room_ids.add(room_id)
        for room in rooms['rows'][:]:
            if room[0] in booked_room_ids:
                rooms['rows'].remove(room)
        data = json.dumps(rooms)
        return data
    