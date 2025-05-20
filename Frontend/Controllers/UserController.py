from Views.UserView import UserView
from Models.Translator import Translator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout
import websockets
import asyncio
import json
import random

class UserController:
    __user_view: UserView
    __add_room_pressed: bool = False
    __add_client_pressed: bool = False
    __add_users_pressed: bool = False
    __user_type:int = 1
    __uri: str = "ws://localhost:8765"

    def __init__(self, SwitchToClientViewCallback = None):
        self.__user_view = UserView()
        self.__SwitchToClientViewCallback = SwitchToClientViewCallback
        self.EventInitializer()

    async def __SendRequest(self, request: str) -> str:
        async with websockets.connect(self.__uri) as websocket:
            await websocket.send(request)
            response = await websocket.recv()
            return response
        
    def __GetRooms(self) -> list[list[str]]:
        response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "ListAvailableRooms"})))
        rooms = Translator.DecodeRoomJSON(response_data)
        return rooms
    
    
    def ShowRooms(self) -> None:
        self.__user_view.Update(self.__GetRooms())

    def EventInitializer(self) -> None:
        self.__user_view.SetLoginFunction(self.Login)
        self.__user_view.SetFilterFunction(self.ShowFilteredRooms)
        self.__user_view.SetAddFunction(self.AddRoom)
        self.__user_view.SetUpdateFunction(self.UpdateRoom)
        self.__user_view.SetDeleteFunction(self.DeleteRoom)
        self.__user_view.SetAddClientFunction(self.AddClient)
        self.__user_view.SetUpdateClientFunction(self.UpdateClient)
        self.__user_view.SetDeleteClientFunction(self.DeleteClient)
        self.__user_view.SetRoomFloorsFunction(self.SetRoomFloorGraphics)
        self.__user_view.SetRoomCitiesFunction(self.SetRoomCitiesGraphics)
        self.__user_view.SetSaveDataFunction(self.SaveData)
        self.__user_view.SetTabChangedFunction(self.TabChanged)
        self.__user_view.SetListUserFunction(self.__GetFilteredUsers)
        self.__user_view.SetAddUserFunction(self.AddUser)
        self.__user_view.SetUpdateUserFunction(self.UpdateUser)
        self.__user_view.SetDeleteUserFunction(self.DeleteUser)
        self.__user_view.SetReserveRoomButtonFunction(self.ReserveRoom)
        self.__user_view.SetLogoutButtonFunction(self.Logout)

    def Login(self) -> None:
        username: str = self.__user_view.GetUsernameInput()
        password: str = self.__user_view.GetPasswordInput()
        response_data = json.loads(asyncio.run(self.__SendRequest(json.dumps({"command": "CheckCredentials", 
                                                                   "username": username, 
                                                                   "password": password}))))
        try:
            self.__user_type = int(response_data['role'])
            self.__user_view.SetUserAuthenticated()
            self.__user_view.HideLoginWidget()
            self.__user_view.ShowTable()
            self.__user_view.ShowControlWidget()
            self.__user_view.HideMainTab()
            self.TabChanged(0)
            self.ShowRooms()
            self.ShowClients()
            self.ShowUsers()
        except (TypeError, KeyError) as e:
            print(e)
            print("Invalid username or password!")
            self.__user_view.SetUsernameInput("")
            self.__user_view.SetPasswordInput("")
            self.__user_view.SetFocusOnUsername()
    
    def Logout(self) -> None:
        self.__user_view.SetUserUnauthenticated()
        self.__user_view.SetUsernameInput("")
        self.__user_view.SetPasswordInput("")
        self.__user_view.SetFocusOnUsername()
        self.__SwitchToClientViewCallback()

    def AddRoom(self) -> None:
        if not self.__add_room_pressed:
            self.__user_view.InsertRow()
            self.__add_room_pressed = True
        else:
            try:
                new_row: int = int(self.__user_view.GetRowCount() - 1)
                new_room_id: int = int(self.__user_view.GetTableItem(new_row, 0))
                new_hotel_name: str = self.__user_view.GetTableItem(new_row, 1)
                new_number: int = int(self.__user_view.GetTableItem(new_row, 2))
                new_location: str = self.__user_view.GetTableItem(new_row, 3)
                new_price: float = float(self.__user_view.GetTableItem(new_row, 4))
                new_position: str = self.__user_view.GetTableItem(new_row, 5)
                new_facilities: str = self.__user_view.GetTableItem(new_row, 6)
                command: str = "AddRoom"

                add_room = Translator.CodeRoomJSON(new_room_id, new_hotel_name, 
                                                   new_number, new_location, new_price, 
                                                   new_position, new_facilities,
                                                   command)
                print(json.loads(asyncio.run(self.__SendRequest(add_room))))
                self.ShowRooms()
                self.__add_room_pressed = False
            except (AttributeError, ValueError) as e:
                print(e)
                return

    def DeleteRoom(self) -> None:
        selected_row: int = self.__user_view.GetCurrentRow()
        try:
            room_id: str = self.__user_view.GetTableItem(selected_row, 0)
            command: str = "DeleteRoom"
            request: str = Translator.CodeReadDeleteRoomJSON(int(room_id), command) 
            print(json.loads(asyncio.run(self.__SendRequest(request))))
            self.ShowRooms()
        except AttributeError:
            self.__user_view.RemoveRow(selected_row)
            self.__add_room_pressed = False

    def UpdateRoom(self) -> None:
        selected_row: int = -1
        selected_row = self.__user_view.GetCurrentRow()

        if selected_row == -1:
            print("No row selected!")
            return
       
        try:
            rooms = self.__GetRooms()
            old_room_id: int = rooms[int(selected_row)][0]
        except IndexError:
            print("No room found!\nYou are probably trying to add a room.")
            return  
         
        try:
            update_room_id: int = int(self.__user_view.GetTableItem(selected_row, 0))
            update_hotel_name: str = self.__user_view.GetTableItem(selected_row, 1)
            update_number: int = int(self.__user_view.GetTableItem(selected_row, 2))
            update_location: str = self.__user_view.GetTableItem(selected_row, 3)
            update_price: float = float(self.__user_view.GetTableItem(selected_row, 4))
            update_position: str = self.__user_view.GetTableItem(selected_row, 5)
            update_facilities: str = self.__user_view.GetTableItem(selected_row, 6)
            command: str = "UpdateRoom"
            update_room: str = Translator.CodeRoomJSON(update_room_id, update_hotel_name, 
                                                  update_number,update_location, update_price,
                                                  update_position, update_facilities, command, old_room_id)
            print(json.loads(asyncio.run(self.__SendRequest(update_room))))
            self.ShowRooms()
        except ValueError as e:
            print("Please fill in all fields correctly!")
            return

    def ShowFilteredRooms(self) -> None:
        if self.__add_room_pressed:
            return
        
        location: str = self.__user_view.GetLocationInput()
        price: str = self.__user_view.GetPriceInput()
        position: str = self.__user_view.GetPositionInput()
        facilities: str = self.__user_view.GetFacilitiesInput()
        if price:
            price: float = float(price)
        else:
            price: None = None

        try:
            filter_rooms = Translator.CodeFilterRoomJSON(location, price, 
                                                        position, facilities)
            response_data = asyncio.run(self.__SendRequest(filter_rooms))
            rooms = Translator.DecodeRoomJSON(response_data)
            self.__user_view.Update(rooms)
            return
        except ValueError as e:
            print(e) 

    def __GetClients(self) -> list[list[str]]:
        response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "ListClients"})))
        clients = Translator.DecodeClientJSON(response_data)
        return clients
       
    def ShowClients(self) -> None:
        self.__user_view.UpdateClients(self.__GetClients())

    def AddClient(self) -> None:
        if not self.__add_client_pressed:
            self.__user_view.InsertClientRow()
            self.__add_client_pressed = True
        else:
            try:
                new_row: int = self.__user_view.GetClientRowCount() - 1
                new_client_id: str = self.__user_view.GetClientTableItem(new_row, 0)
                new_client_name: str = self.__user_view.GetClientTableItem(new_row, 1)
                new_client_email: str = self.__user_view.GetClientTableItem(new_row, 2)
                new_client_phone_number: str = self.__user_view.GetClientTableItem(new_row, 3)
                command: str = "AddClient"

                add_client = Translator.CodeClientJSON(int(new_client_id), new_client_name, 
                                                      new_client_email, new_client_phone_number, command)
                                                   
                print(json.loads(asyncio.run(self.__SendRequest(add_client))))
                self.ShowClients()
                self.__add_client_pressed = False
            except (AttributeError, ValueError) as e:
                print(e)
                return
            
    def UpdateClient(self) -> None:
        selected_row: int = -1
        selected_row = self.__user_view.GetCurrentClientRow()

        if selected_row == -1:
            print("No row selected!")
            return
        
        try:
            clients = self.__GetClients()
            old_client_id: int = clients[selected_row][0]
        except IndexError:
            print("No room found!\nYou are probably trying to add a room.")
            return   

        try:
            new_client_id: str = self.__user_view.GetClientTableItem(selected_row, 0)
            new_client_name: str = self.__user_view.GetClientTableItem(selected_row, 1)
            new_client_email: str = self.__user_view.GetClientTableItem(selected_row, 2)
            new_client_phone_number: str = self.__user_view.GetClientTableItem(selected_row, 3)
            command: str = "UpdateClient"

            update_client: str = Translator.CodeClientJSON(int(new_client_id), new_client_name, 
                                                       new_client_email, new_client_phone_number, 
                                                       command, int(old_client_id))
            
            print(json.loads(asyncio.run(self.__SendRequest(update_client))))
            self.ShowClients()
        except ValueError as e:
            print("Please fill in all fields correctly!")
            return
        
    def DeleteClient(self) -> None:
        selected_row: int = self.__user_view.GetCurrentClientRow()
        try:
            client_id: str = self.__user_view.GetClientTableItem(selected_row, 0)
            command: str = "DeleteClient"
            delete_client: str = Translator.CodeReadDeleteClientJSON(int(client_id), command) 
            print(json.loads(asyncio.run(self.__SendRequest(delete_client))))
            self.ShowClients()
        except AttributeError:
            self.__user_view.RemoveClientRow(selected_row)
            self.__add_room_pressed = False

    def __ClearGraphicZone(self) -> None:
        gr_zone = self.__user_view.GetGraphicZone()
        layout = gr_zone.layout()
        if layout is not None:
            layout.itemAt(0).widget().setParent(None)
        else:
            layout = QVBoxLayout()
            gr_zone.setLayout(layout)

    def SetRoomCitiesGraphics(self) -> None:
        command = json.dumps({"command": "CitiesStats"})
        sizes, labels = json.loads(asyncio.run(self.__SendRequest(command)))
        colors = random.sample(plt.cm.tab10.colors, len(sizes))
        
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.barh(labels, sizes, color=colors)
        canvas = FigureCanvas(fig)

        self.__ClearGraphicZone()
        self.__user_view.SetGraphicZone(canvas)
        plt.close(fig)
    
    def SetRoomFloorGraphics(self) -> None:
        command = json.dumps({"command": "RoomFloorStats"})
        sizes, labels = json.loads(asyncio.run(self.__SendRequest(command)))
        colors = random.sample(plt.cm.tab10.colors, len(sizes))
        

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.bar(labels, sizes, color=colors)
        canvas = FigureCanvas(fig)

        self.__ClearGraphicZone()
        self.__user_view.SetGraphicZone(canvas)
        plt.close(fig)

    def SaveData(self) -> None:
        file_format = self.__user_view.GetDropdownValue()
        response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "SaveData", "file_format": file_format})))
        with open(f"saved_data.{file_format.lower()}", "w") as f:
            f.write(response_data)
        print(f"Data saved as {file_format}.")
    
    def TabChanged(self, index: int) -> None:
        if index == 3:
            if self.__user_type == 1:
                self.__user_view.ShowAdminTabMessage(False)
            else:
                self.__user_view.ShowAdminTabMessage(True)
        else:
            if self.__user_type == 1:
                self.__user_view.ShowUserTabMessage(True)
            else:
                self.__user_view.ShowUserTabMessage(False)
    
    def __GetUsers(self) -> list[list[str]]:
        response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "ListUsers"})))
        users = Translator.DecodeUserJSON(response_data)
        return users
    
    def __GetFilteredUsers(self) -> list[list[str]]:
        filter: int = None
        if (self.__user_view.GetUserRoleDropdownValue()):
            filter = 1 if self.__user_view.GetUserRoleDropdownValue() == "Admin" else 2
            response_data = asyncio.run(self.__SendRequest(json.dumps({"command": "ListUsers", "filter": filter})))
            users = Translator.DecodeUserJSON(response_data)
            self.__user_view.UpdateUsers(users)
        else:
            self.ShowUsers()
       
    def ShowUsers(self) -> None:            
        self.__user_view.UpdateUsers(self.__GetUsers())

    def AddUser(self) -> None:
        if not self.__add_users_pressed:
            self.__user_view.InsertUserRow()
            self.__add_users_pressed = True
        else:
            try:
                new_row: int = self.__user_view.GetUserRowCount() - 1
                new_user_id: str = self.__user_view.GetUserTableItem(new_row, 0)
                new_username: str = self.__user_view.GetUserTableItem(new_row, 1)
                new_password: str = self.__user_view.GetUserTableItem(new_row, 2)
                new_user_role: int = self.__user_view.GetUserTableItem(new_row, 3)
                command: str = "AddUser"

                add_user = Translator.CodeUserJSON(int(new_user_id), new_username, 
                                                      new_password, int(new_user_role),
                                                      command)
                print(json.loads(asyncio.run(self.__SendRequest(add_user))))
                self.ShowUsers()
                self.__add_users_pressed = False
            except (AttributeError, ValueError) as e:
                print(e)
                return
            
    def DeleteUser(self) -> None:
        selected_row: int = self.__user_view.GetCurrentUserRow()
        try:
            user_id: str = self.__user_view.GetUserTableItem(selected_row, 0)
            command: str = "DeleteUser"
            delete_user: str = Translator.CodeReadDeleteUserJSON(int(user_id), command) 
            print(json.loads(asyncio.run(self.__SendRequest(delete_user))))
            self.ShowUsers()
        except AttributeError:
            self.__user_view.RemoveUserRow(selected_row)
            self.__add_user_pressed = False

    def UpdateUser(self) -> None:
        selected_row: int = -1
        selected_row = self.__user_view.GetCurrentUserRow()

        if selected_row == -1:
            print("No row selected!")
            return
        
        try:
            users = self.__GetUsers()
            old_user_id: int = users[selected_row][0]
        except IndexError:
            print("No room found!\nYou are probably trying to add a room.")
            return   

        try:
            new_user_id: str = self.__user_view.GetUserTableItem(selected_row, 0)
            new_username: str = self.__user_view.GetUserTableItem(selected_row, 1)
            new_password: str = self.__user_view.GetUserTableItem(selected_row, 2)
            new_user_role: int = self.__user_view.GetUserTableItem(selected_row, 3)
            command: str = "UpdateUser"

            update_user = Translator.CodeUserJSON(int(new_user_id), new_username, 
                                               new_password, int(new_user_role),
                                               command, old_user_id)
            print(json.loads(asyncio.run(self.__SendRequest(update_user))))
            self.ShowUsers()
        except ValueError as e:
            print("Please fill in all fields correctly!")
            return
        
    def ReserveRoom(self) -> None:
        start_date: str = self.__user_view.GetStartDate()
        end_date: str = self.__user_view.GetEndDate()
        client_id: int = int(self.__user_view.GetClientIdInput())
        selected_row = self.__user_view.GetCurrentRow()
        room_id: str = int(self.__user_view.GetTableItem(selected_row, 0))

        add_booking = json.dumps({
                "command": "AddBooking",
                "booking": {
                    "start_date": start_date,
                    "end_date": end_date,
                    "client_id": client_id,
                    "room_id": room_id
                }
        })
        print(json.loads(asyncio.run(self.__SendRequest(add_booking))))
        self.ShowRooms()
        
    def GetGUI(self) -> UserView:
        return self.__user_view