from Domain.User import User

class IUserRepository:
    def CreateUser(self, user: User) -> None:
        pass

    def UpdateUser(self, old_User_id: int, user: User) -> None:
        pass

    def DeleteUser(self, User_id: int) -> None:
        pass

    def ListUsers(self, filter: int = None) -> dict:
        pass

    def CheckCredentials(self, username: str, password: str) -> int:
        pass

