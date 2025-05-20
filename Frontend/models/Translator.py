import json

class Translator:
    def CodeRoomJSON(id: int, hotel_name: str, room_number: int, location: str,
                       price: float, position: str, facilities: str,
                       command: str = None, old_room_id: int = None) -> str:
        result  = {}
        if command:
            result["command"] = command
        if old_room_id:
            result["old_room_id"] = old_room_id
        result["room"] = {
                "room_id": id,
                "hotel_name": hotel_name,
                "number": room_number,
                "location": location,
                "price": price,
                "position": position,
                "facilities": facilities
            }   
        return json.dumps(result)
    
    def CodeFilterRoomJSON(location: str = None, 
                           price: str = None, 
                           position: str = None, 
                           facilities: str = None) -> str:
        filter_rooms = {
                "command": "FilterRooms",
                "criteria": {
                    "location": location if location else "",
                    "price": price if price else "",
                    "position": position if position else "",
                    "facilities": facilities if facilities else ""
                }
        }
        return json.dumps(filter_rooms)
    
    def CodeFilterRoomClientJSON(location: str = None, 
                        price: str = None, 
                        position: str = None, 
                        facilities: str = None) -> str:
        filter_rooms = {
                "command": "FilterRoomsClient",
                "criteria": {
                    "location": location if location else "",
                    "price": price if price else "",
                    "position": position if position else "",
                    "facilities": facilities if facilities else ""
                }
        }
        return json.dumps(filter_rooms)
    
    def CodeReadDeleteRoomJSON(room_id: int, command: str) -> str:
        request = {
            "command": command,
            "room_id": room_id
        }

        return json.dumps(request)

    def DecodeRoomJSON(json_str: str) -> list[list[str]]:
        json_str = json.loads(json_str)
        return json_str["rows"]
    
    def CodeClientJSON(client_id:str , client_name: str, client_email: str, 
                        client_phone_number: str, command: str = None, 
                        old_client_id: str = None) -> str:
        result  = {}
        if command:
            result["command"] = command
        if old_client_id:
            result["old_client_id"] = old_client_id
        result["client"] = {
                "client_id": client_id,
                "client_name": client_name,
                "client_email": client_email,
                "client_phone_number": client_phone_number,
            }   
        return json.dumps(result)
    
        
    def CodeReadDeleteClientJSON(client_id: int, command: str) -> str:
        request = {
            "command": command,
            "client_id": client_id
        }

        return json.dumps(request)
    
    def DecodeClientJSON(json_str: str) -> list[list[str]]:
        json_str = json.loads(json_str)
        return json_str["rows"]
    
    def CodeUserJSON(user_id:int , username: str, password: str, role: int,
                        command: str = None, old_user_id: int = None) -> str:
        result  = {}
        if command:
            result["command"] = command
        if old_user_id:
            result["old_user_id"] = old_user_id
        result["user"] = {
                "user_id": user_id,
                "username": username,
                "password": password,
                "role": role,
            }   
        return json.dumps(result)
        
    def CodeReadDeleteUserJSON(user_id: int, command: str) -> str:
        request = {
            "command": command,
            "user_id": user_id
        }

        return json.dumps(request)
    
    def DecodeUserJSON(json_str: str) -> list[list[str]]:
        json_str = json.loads(json_str)
        return json_str["rows"]
        