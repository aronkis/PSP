from Domain.IRoomRepository import IRoomRepository
from Repositories.Repository import Repository
from Domain.Room import Room
import json

class RoomRepository(IRoomRepository):
    def __init__(self):
        self.__room_repository: Repository = Repository()

    def CreateRoom(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Expected a Room object.")
        self.__room_repository.ModifyData(""" INSERT INTO Room (id, hotel_name, number, price, location, position, facilities) VALUES (?, ?, ?, ?, ?, ?, ?) """, \
                       (room.GetId(), room.GetHotelName(), room.GetNumber(), room.GetPrice(), room.GetLocation(), room.GetPosition(), room.GetFacilities()))
    
    def UpdateRoom(self, old_room_id: str, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Expected a Room object.")
        self.__room_repository.ModifyData("""
            UPDATE Room SET id=?, hotel_name=?, number=?, price=?, location=?, position=?, facilities=?
            WHERE id=?""", (room.GetId(), room.GetHotelName(), room.GetNumber(), room.GetPrice(), room.GetLocation(), room.GetPosition(), room.GetFacilities(), old_room_id))

    def DeleteRoom(self, room_id: int) -> None:
        self.__room_repository.ModifyData("DELETE FROM Room WHERE id=?", (room_id, ))

    def ListRooms(self) -> dict:
        data: str = self.__room_repository.GetData("SELECT * FROM Room")
        return json.loads(data)
    
    def FilterRooms(self,
        location: str = None,
        price: float = None,
        position: str = None,
        facilities: str = None
    ) -> dict:
        query: str = "SELECT * FROM Room WHERE 1=1"
        params: list = []
        filtered: bool = False

        if location:
            query += " AND location=?"
            params.append(location)
            filtered = True
        if price:
            query += " AND price <= ?"
            params.append(price)
            filtered = True
        if position:
            query += " AND position=?"
            params.append(position)
            filtered = True
        if facilities:
            query += " AND facilities LIKE ?"
            params.append(f"%{facilities}%")
            filtered = True

        if filtered:
            data:json = self.__room_repository.GetDataWithParams(query, params)
            return json.loads(data)
        else:
            data: json = self.ListRooms()
            return json.loads(json.dumps(data))