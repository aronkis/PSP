from Domain.Room import Room

class IRoomRepository:
    def CreateRoom(self, room: Room) -> None:
        pass

    def UpdateRoom(self, old_room_id: int, room: Room) -> None:
        pass

    def DeleteRoom(self, room_id: int) -> None:
        pass

    def ListRooms(self) -> dict:
        pass

    def FilterRooms(self) -> dict:
        pass