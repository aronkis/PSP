from Services.IAdminServices import IAdminServices
from Repositories.UserRepository import UserRepository
from Domain.IUserRepository import IUserRepository
from Domain.User import User
import json

class AdminServices(IAdminServices):
    def __init__(self):
        self.__user_repository: IUserRepository = UserRepository()

    def AddUser(self, user_data: str) -> None:
        self.__user_repository.CreateUser(User(**user_data))

    def UpdateUser(self, old_user_id: int, user_data: str) -> None:
        self.__user_repository.UpdateUser(old_user_id, User(**user_data))

    def DeleteUser(self, user_id: int) -> None:
        self.__user_repository.DeleteUser(user_id)

    def ListUsers(self, filter: int = None):
        users: dict = self.__user_repository.ListUsers(filter)
        return json.dumps(users)      
    
    def CheckCredentials(self, username: str, password: str) -> int:
        return self.__user_repository.CheckCredentials(username, password)
