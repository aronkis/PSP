import asyncio
from websockets.legacy.server import WebSocketServerProtocol
from websockets import serve, ConnectionClosed
import json
from typing import Any, Set, Dict, Coroutine

from Services.EmployeeServices import EmployeeServices
from Services.IEmployeeServices import IEmployeeServices
from Services.IAdminServices import IAdminServices
from Services.AdminServices import AdminServices
from Services.IClientServices import IClientServices
from Services.ClientServices import ClientServices

class WebSocketServer:
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.HOST: str = host
        self.PORT: int = port
        self.employee_services: IEmployeeServices = EmployeeServices()
        self.admin_services: IAdminServices = AdminServices()
        self.client_services: IClientServices = ClientServices()
        self.connected_clients: Set[WebSocketServerProtocol] = set()

    async def send_json(self, websocket: WebSocketServerProtocol, data: Any) -> Coroutine[Any, Any, None]:
        await websocket.send(json.dumps(data))

    async def handle_room_commands(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]) -> bool:
        match data.get("command"):
            case "ListAvailableRoomsClient":
                await websocket.send(self.client_services.ListAvailableRooms())
            case "FilterRoomsClient":
                criteria: Dict[str, Any] = data.get("criteria", {})
                await websocket.send(self.client_services.FilterRooms(**criteria))
            case "ListAvailableRooms":
                await websocket.send(self.employee_services.ListAvailableRooms())
            case "FilterRooms":
                criteria: Dict[str, Any] = data.get("criteria", {})
                await websocket.send(self.employee_services.FilterRooms(**criteria))
            case "AddRoom":
                room_data: Any = data.get("room")
                if room_data:
                    self.employee_services.AddRoom(room_data)
                    await self.send_json(websocket, {"Success": "Room added"})
                else:
                    await self.send_json(websocket, {"error": "Invalid room data"})
            case "ReadRoom":
                room_id: Any = data.get("room_id")
                await self.send_json(websocket, self.employee_services.ReadRoom(room_id))
            case "UpdateRoom":
                room_data: Any = data.get("room")
                old_room_id: Any = data.get("old_room_id")
                if room_data:
                    self.employee_services.UpdateRoom(old_room_id, room_data)
                    await self.send_json(websocket, {"Success": "Room updated"})
                else:
                    await self.send_json(websocket, {"error": "Invalid room data"})
            case "DeleteRoom":
                room_id: Any = data.get("room_id")
                if room_id:
                    self.employee_services.DeleteRoom(room_id)
                    await self.send_json(websocket, {"Success": "Room deleted."})
                else:
                    await self.send_json(websocket, {"error": "Invalid room ID"})
            case _:
                return False
        return True

    async def handle_client_commands(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]) -> bool:
        match data.get("command"):
            case "ListClients":
                await websocket.send(self.employee_services.ListClients())
            case "AddClient":
                client_data: Any = data.get("client")
                if client_data:
                    self.employee_services.AddClient(client_data)
                    await self.send_json(websocket, {"Success": "Client added"})
                else:
                    await self.send_json(websocket, {"error": "Invalid client data"})
            case "UpdateClient":
                client_data: Any = data.get("client")
                old_client_id: Any = data.get("old_client_id")
                if client_data:
                    self.employee_services.UpdateClient(old_client_id, client_data)
                    await self.send_json(websocket, {"Success": "Client updated"})
                else:
                    await self.send_json(websocket, {"error": "Invalid Client data"})
            case "DeleteClient":
                client_id: Any = data.get("client_id")
                if client_id:
                    self.employee_services.DeleteClient(client_id)
                    await self.send_json(websocket, {"Success": "Client deleted."})
                else:
                    await self.send_json(websocket, {"error": "Invalid Client ID"})
            case _:
                return False
        return True

    async def handle_stats_commands(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]) -> bool:
        match data.get("command"):
            case "CitiesStats":
                cities_count: Any = self.employee_services.GetGraphics(3)
                await self.send_json(websocket, cities_count)
            case "RoomFloorStats":
                floor_count: Any = self.employee_services.GetGraphics(5)
                await self.send_json(websocket, floor_count)
            case _:
                return False
        return True

    async def handle_user_commands(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]) -> bool:
        match data.get("command"):
            case "ListUsers":
                filter: Any = data.get("filter")
                await websocket.send(self.admin_services.ListUsers(filter))
            case "AddUser":
                user_data: Any = data.get("user")
                if user_data:
                    self.admin_services.AddUser(user_data)
                    await self.send_json(websocket, {"Success": "User added"})
                else:
                    await self.send_json(websocket, {"error": "Invalid user data"})
            case "UpdateUser":
                user_data: Any = data.get("user")
                old_user_id: Any = data.get("old_user_id")
                if user_data:
                    self.admin_services.UpdateUser(old_user_id, user_data)
                    await self.send_json(websocket, {"Success": "User updated"})
                else:
                    await self.send_json(websocket, {"error": "Invalid User data"})
            case "DeleteUser":
                user_id: Any = data.get("user_id")
                if user_id:
                    self.admin_services.DeleteUser(user_id)
                    await self.send_json(websocket, {"Success": "User deleted."})
                else:
                    await self.send_json(websocket, {"error": "Invalid user ID"})
            case "CheckCredentials":
                username: Any = data.get("username")
                password: Any = data.get("password")
                if username and password:
                    role: Any = self.admin_services.CheckCredentials(username, password)
                    await self.send_json(websocket, {"role": role})
                else:
                    await self.send_json(websocket, {"error": "Invalid username or password"})
            case _:
                return False
        return True

    async def handle_misc_commands(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]) -> bool:
        match data.get("command"):
            case "SaveData":
                file_format: Any = data.get("file_format")
                response: Any = self.employee_services.SaveData(file_format)
                await websocket.send(response)
            case "AddBooking":
                booking_data: Any = data.get("booking")
                self.employee_services.AddBooking(booking_data)
                await self.send_json(websocket, {"Success": "Booking created"})
            case _:
                return False
        return True

    async def handle_connection(self, websocket: WebSocketServerProtocol) -> None:
        self.connected_clients.add(websocket)
        try:
            async for message in websocket:
                try:
                    data: Dict[str, Any] = json.loads(message)
                    handled: bool = (
                        await self.handle_room_commands(websocket, data) or
                        await self.handle_client_commands(websocket, data) or
                        await self.handle_stats_commands(websocket, data) or
                        await self.handle_user_commands(websocket, data) or
                        await self.handle_misc_commands(websocket, data)
                    )
                    if not handled:
                        await self.send_json(websocket, {"error": "Unknown command"})
                except json.JSONDecodeError:
                    await self.send_json(websocket, {"error": "Invalid JSON format"})
                except Exception as e:
                    await self.send_json(websocket, {"Exception caught": str(e)})
        except ConnectionClosed as e:
            print(f"Connection closed: {e}")
        finally:
            self.connected_clients.remove(websocket)

    async def start(self) -> None:
        print(f"Starting WebSocket server at ws://{self.HOST}:{self.PORT}")
        async with serve(self.handle_connection, self.HOST, self.PORT):
            await asyncio.Future()

if __name__ == "__main__":
    server = WebSocketServer()
    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("Server stopped")