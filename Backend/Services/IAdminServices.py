class IAdminServices:
    def AddUser(self, user_data: str) -> None:
        pass

    def UpdateUser(self, old_user_id: int, user_data: str) -> None:
        pass

    def DeleteUser(self, user_id: int) -> None:
        pass

    def ListUsers(self, filter: int = None) -> str:
        pass

    def CheckCredentials(self, username: str, password: str) -> int:
        pass
