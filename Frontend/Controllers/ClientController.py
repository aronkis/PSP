from Views.ClientView import ClientView
from Models.Translator import Translator
import websockets
import asyncio
import json

class ClientController:
    __client_view: ClientView
    __uri: str = "ws://localhost:8765"

    def __init__(self, SwitchToUserViewCallback = None):
        self.__client_view = ClientView()
        self.__SwitchToUserViewCallback = SwitchToUserViewCallback
        self.EventInitializer()
        self.ShowRooms()

    async def __SendRequest(self, request: str) -> str:
        async with websockets.connect(self.__uri) as websocket:
            await websocket.send(request)
            response = await websocket.recv()
            return response
        
    def __GetRooms(self) -> list[list[str]]:
        response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "ListAvailableRoomsClient"})))
        rooms = Translator.DecodeRoomJSON(response_data)
        return rooms
    
    def ShowRooms(self) -> None:
        self.__client_view.Update(self.__GetRooms())

    def EventInitializer(self) -> None:
        self.__client_view.SetFilterFunctionClient(self.ShowFilteredRoomsClient)
        self.__client_view.SetLoginFunctionClient(self.HandleLogin)

    def HandleLogin(self):
            self.__SwitchToUserViewCallback()

    def ShowFilteredRoomsClient(self) -> None:
        location: str = self.__client_view.GetLocationInputClient()
        price: str = self.__client_view.GetPriceInputClient()
        position: str = self.__client_view.GetPositionInputClient()
        facilities: str = self.__client_view.GetFacilitiesInputClient()
        if price:
            price: float = float(price)
        else:
            price: None = None

        try:
            filter_rooms = Translator.CodeFilterRoomClientJSON(location, price, 
                                                        position, facilities)
            response_data = asyncio.run(self.__SendRequest(filter_rooms))
            rooms = Translator.DecodeRoomJSON(response_data)
            self.__client_view.Update(rooms)
            return
        except ValueError as e:
            print(e) 
        
    def GetGUI(self) -> ClientView:
        return self.__client_view