class IClientServices:
    def ListAvailableRooms(self) -> str:
        pass
    
    def FilterRooms(self,
        location: str = None,
        price: float = None,
        position: str = None,
        facilities: str = None) -> str:
        pass