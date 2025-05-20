class Room:
    def __init__(self, room_id: int, hotel_name: str, number: int, location: str, 
                 price: float, position: str, facilities: str):
        if not isinstance(room_id, int) or room_id <= 0:
            raise ValueError("Room ID must be a positive integer.")
        self.__id: int = room_id

        if not isinstance(hotel_name, str) or not hotel_name.strip():
            raise ValueError("Hotel name must be a non-empty string.")
        self.__hotel_name: str = hotel_name

        if not isinstance(number, int) or number <= 0:
            raise ValueError("Room number must be a positive integer.")
        self.__number: int = number

        if not isinstance(location, str) or not location.strip():
            raise ValueError("Location must be a non-empty string.")
        self.__location: str = location

        if not isinstance(price, float) or price <= 0:
            raise ValueError("Price must be a positive number.")
        self.__price: float = price

        if not isinstance(position, str) or not position.strip():
            raise ValueError("Position must be a non-empty string.")
        self.__position: str = position

        if not isinstance(facilities, str) or not facilities.strip():
            raise ValueError("Facilities must be a non-empty string.")
        self.__facilities: str = facilities

    def GetId(self) -> int:
        return self.__id

    def GetHotelName(self) -> str:
        return self.__hotel_name

    def GetNumber(self) -> int:
        return self.__number

    def GetLocation(self) -> str:
        return self.__location

    def GetPrice(self) -> float:
        return self.__price

    def GetPosition(self) -> str:
        return self.__position

    def GetFacilities(self) -> str:
        return self.__facilities

    def SetId(self, room_id: int) -> None:
        if not isinstance(room_id, int):
            raise ValueError("Room ID must be an integer.")
        if room_id <= 0:
            raise ValueError("Room ID must be a positive integer.")
        if self.__id is not None:
            self.__id = room_id

    def SetHotelName(self, hotel_name: str) -> None:
        if not isinstance(hotel_name, str):
            raise ValueError("Hotel name must be a string.")
        if not hotel_name.strip():
            raise ValueError("Hotel name cannot be empty.")
        self.__hotel_name = hotel_name

    def SetNumber(self, number: int) -> None:
        if not isinstance(number, int):
            raise ValueError("Room number must be an integer.")
        if number <= 0:
            raise ValueError("Room number must be a positive integer.")
        self.__number = number

    def SetLocation(self, location: str) -> None:
        if not isinstance(location, str):
            raise ValueError("Location must be a string.")
        if not location.strip():
            raise ValueError("Location cannot be empty.")
        self.__location = location

    def SetPrice(self, price: float) -> None:
        if not isinstance(price, float):
            raise ValueError("Price must be a number.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.__price = price

    def SetPosition(self, position: str) -> None:
        if not isinstance(position, str):
            raise ValueError("Position must be a string.")
        if not position.strip():
            raise ValueError("Position cannot be empty.")
        self.__position = position

    def SetFacilities(self, facilities: str) -> None:
        if not isinstance(facilities, str):
            raise ValueError("Facilities must be a string.")
        if not facilities.strip():
            raise ValueError("Facilities cannot be empty.")
        self.__facilities = facilities