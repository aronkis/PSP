class IEmployeeServices:
    def ListAvailableRooms(self) -> str:
        pass
    
    def FilterRooms(self,
        location: str = None,
        price: float = None,
        position: str = None,
        facilities: str = None) -> str:
        pass
    
    def AddRoom(self, room_data: str) -> None:
        pass

    def UpdateRoom(self, old_room_id: str, room_data: str) -> None:
        pass
    
    def DeleteRoom(self, room_id: int) -> None:
        pass

    def AddBooking(self, booking_data: str) -> None:
        pass

    def CreateClient(self, client_data: str) -> None:
        pass

    def UpdateClient(self, old_client_id: int, client_data: str) -> None:
        pass

    def DeleteClient(self, client_id: int) -> None:
        pass

    def ListClients(self) -> str:
        pass

    def GetGraphics(self, column_number: int) -> tuple:
        pass

    def SaveData(self, file_format: str) -> str:
        pass