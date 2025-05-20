from Domain.IUserRepository import IUserRepository
from Repositories.Repository import Repository
from Domain.User import User
import json

class UserRepository(IUserRepository):

    def __init__(self):
        self.__user_repository: Repository = Repository()

    def CreateUser(self, user: User) -> None:
        if not isinstance(user, User):
            raise ValueError("Expected a User object.")
        
        self.__user_repository.ModifyData("""INSERT INTO User (id, username, password, role) VALUES (?, ?, ?, ?)""",
                                (user.GetId(), user.GetUsername(), user.GetPassword(), user.GetRole()))
    
    def UpdateUser(self, old_user_id: int, user: User) -> None:
        if not isinstance(user, User):
            raise ValueError("Expected a User object.")
        
        self.__user_repository.ModifyData("""UPDATE User SET id = ?, username = ?, password = ?, role = ? WHERE id = ?""",
                                (user.GetId(), user.GetUsername(), user.GetPassword(), user.GetRole(), old_user_id))

    def DeleteUser(self, user_id: int) -> None:
        self.__user_repository.ModifyData("DELETE FROM User WHERE id=?", (user_id, ))

    def ListUsers(self, filter: int = None) -> dict:
        if filter is not None and not isinstance(filter, int):
            raise ValueError("Filter should be an integer")
        
        if filter is not None:
            query = "SELECT * FROM User WHERE role=?"
            result = self.__user_repository.GetDataWithParams(query, (filter,))
            if result:
                return json.loads(result)
            else:
                raise ValueError(f"No users found with role {filter}")
        else:
            data: str = self.__user_repository.GetData("SELECT * FROM User")
            return json.loads(data)
        
    def CheckCredentials(self, username: str, password: str) -> int:
        if not isinstance(username, str):
            raise ValueError("Username should be a string.")
        if not isinstance(password, str):
            raise ValueError("String should be a string.")
        
        query = "SELECT * FROM User WHERE username = ? AND password = ?"
        result = json.loads(self.__user_repository.GetDataWithParams(query, (username, password)))
        try:
            result = int(result['rows'][0][3])
        except TypeError:
            result = 0
        return result