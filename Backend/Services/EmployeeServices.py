from Services.IEmployeeServices import IEmployeeServices
from Repositories.BookingRepository import BookingRepository
from Domain.IBookingRepository import IBookingRepository
from Repositories.RoomRepository import RoomRepository
from Domain.IRoomRepository import IRoomRepository
from Repositories.UserRepository import UserRepository
from Domain.IUserRepository import IUserRepository
from Repositories.ClientRepository import ClientRepository
from Domain.IClientRepository import IClientRepository
from Domain.Booking import Booking
from Domain.Client import Client
from Domain.Room import Room
import xml.etree.ElementTree as ET
from datetime import datetime
from io import StringIO
import json
import csv

class EmployeeServices(IEmployeeServices):
    def __init__(self):
        self.__room_repository: IRoomRepository = RoomRepository()
        self.__booking_repository: IBookingRepository = BookingRepository()
        self.__client_repository : IClientRepository = ClientRepository()
    
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
    
    def AddRoom(self, room_data: str) -> None:
        self.__room_repository.CreateRoom(Room(**room_data))

    def UpdateRoom(self, old_room_id: str, room_data: str) -> None:
        self.__room_repository.UpdateRoom(old_room_id, Room(**room_data))
    
    def DeleteRoom(self, room_id: int) -> None:
        self.__room_repository.DeleteRoom(room_id)

    def AddBooking(self, booking_data: str) -> None:
        self.__booking_repository.CreateBooking(Booking(**booking_data))

    def AddClient(self, client_data: str) -> None:
        self.__client_repository.CreateClient(Client(**client_data))

    def UpdateClient(self, old_client_id: int, client_data: str) -> None:
        self.__client_repository.UpdateClient(old_client_id, Client(**client_data))

    def DeleteClient(self, client_id: int) -> None:
        self.__client_repository.DeleteClient(client_id)

    def ListClients(self) -> str:
        clients: dict = self.__client_repository.ListClients()
        return json.dumps(clients)   
    
    def CheckCredentials(self, username: str, password: str) -> int:
        return self.____user_repositorysitory.CheckCredentials(username, password)
    
    def __ListRooms(self) -> str:
        rooms: str = self.__room_repository.ListRooms()
        return json.dumps(rooms)
    
    def GetGraphics(self, column_number: int) -> tuple:
        rooms = json.loads(self.__ListRooms())
        rows = rooms["rows"]
        cities_count = {}
        for row in rows:
            city = row[column_number]
            if city in cities_count:
                cities_count[city] += 1
            else:
                cities_count[city] = 1
        sizes = [value for value in cities_count.values()]
        labels = [key for key in cities_count.keys()]
        return sizes, labels
    
    def __ConvertDate(self, date: int) -> str:
        date_str = str(date)
        if len(date_str) == 8:
            return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
        return date_str

    def SaveData(self, file_format: str) -> str:
        bookings: json = self.__booking_repository.ListBookings()
        columns = bookings["columns"]
        rows = bookings["rows"]
        for row in rows:
            row[1] = self.__ConvertDate(row[1])
            row[2] = self.__ConvertDate(row[2])
        try:
            match file_format:
                case "json":
                    rooms_list = [dict(zip(columns, row)) for row in rows]
                    data = {"Rooms": rooms_list}
                    return json.dumps(data, indent=4)
                case "csv":
                    output = StringIO()
                    writer = csv.writer(output)
                    writer.writerow(columns)
                    writer.writerows(rows)
                    return output.getvalue()
                case "xml":
                    root = ET.Element("Rooms")
                    for row in rows:
                        room_elem = ET.SubElement(root, "Room")
                        for col, value in zip(columns, row):
                            col_elem = ET.SubElement(room_elem, col)
                            col_elem.text = str(value)
                    return ET.tostring(root, encoding="unicode")
                case "txt":
                    output = StringIO()
                    output.write("\t".join(columns) + "\n")
                    for row in rows:
                        output.write("\t".join(str(v) for v in row) + "\n")
                    return output.getvalue()
                case _:
                    return f"Unsupported file format: {file_format}"
        except Exception as e:
            return f"Error serializing data: {e}"
        
if __name__ == "__main__":
    employee_services = EmployeeServices()
    print(employee_services.ListAvailableRooms())
    print(employee_services.FilterRooms(position = "1st floor"))
