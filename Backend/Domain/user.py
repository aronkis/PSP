class User:
    def __init__(self, user_id: int, username: str, password: str, role: int = 2):

        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")
        self.__id: str = user_id

        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")
        self.__username: str = username

        if not isinstance(password, str) or not password.strip():
            raise ValueError("Password must be a non-empty string.")
        self.__password: str = password
        if not isinstance(role, int) or (role != 1 and role != 2):
            raise ValueError("Role must be either 1 (Admin) or 2 (Employee).")
        self.__role: int = role

    def GetId(self) -> int:
        return self.__id
    
    def GetUsername(self) -> str:
        return self.__username
    
    def GetPassword(self) -> str:
        return self.__password
    
    def GetRole(self) -> int:
        return self.__role
    
    def SetId(self, user_id: int) -> None:
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if user_id <= 0:
            raise ValueError("User ID must be a positive integer.")
        self.__id = user_id

    def SetUsername(self, username: str) -> None:
        if not isinstance(username, str):
            raise ValueError("Username must be a string.")
        if not username.strip():
            raise ValueError("Username cannot be empty.")
        self.__username = username

    def SetPassword(self, password: str) -> None:
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")
        if not password.strip():
            raise ValueError("Password cannot be empty.")
        self.__password = password

    def SetRole(self, role: int) -> None:
        if not isinstance(role, int):
            raise ValueError("Role must be an int.")
        if role not in [1, 2]:
            raise ValueError("Role must be either 1 (Admin) or 2 (Employee).")
        self.__role = role