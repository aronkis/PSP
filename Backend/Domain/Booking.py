class Booking:
    def __init__(self, start_date: str, end_date: str,
                 client_id: int, room_id: int):
        if not isinstance(start_date, str) or not start_date.strip():
            raise ValueError("Start date must be a non-empty string.")
        self.__start_date: str = start_date

        if not isinstance(end_date, str) or not end_date.strip():
            raise ValueError("Client email must be a non-empty string.")
        self.__end_date: str = end_date

        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Status number must be a positive integer.")
        self.__client_id: int = client_id

        if not isinstance(room_id, int) or room_id <= 0:
            raise ValueError("Room ID must be a positive integer.")
        self.__room_id: int = room_id

    def GetStartDate(self) -> str:
        return self.__start_date

    def GetEndDate(self) -> str:
        return self.__end_date

    def GetClientId(self) -> int:
        return self.__client_id

    def GetRoomId(self) -> int:
        return self.__room_id
    
    def SetStartDate(self, start_date: str) -> None:
        if not isinstance(start_date, str) or not start_date.strip():
            raise ValueError("Start date must be a non-empty string.")
        self.__start_date = start_date

    def SetEndDate(self, end_date: str) -> None:
        if not isinstance(end_date, str) or not end_date.strip():
            raise ValueError("End date must be a non-empty string.")
        self.__end_date = end_date

    def SetClientId(self, client_id: int) -> None:
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")
        self.__client_id = client_id

    def SetRoomId(self, room_id: int) -> None:
        if not isinstance(room_id, int) or room_id <= 0:
            raise ValueError("Room ID must be a positive integer.")
        self.__room_id = room_id
