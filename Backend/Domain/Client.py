class Client:
    def __init__(self, client_id: int, client_name: str, client_email: str,
                 client_phone_number: str):
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")
        self.__client_id: int = client_id

        if not isinstance(client_name, str) or not client_name.strip():
            raise ValueError("Client name must be a non-empty string.")
        self.__client_name: str = client_name

        if not isinstance(client_email, str) or not client_email.strip():
            raise ValueError("Client email must be a non-empty string.")
        self.__client_email: str = client_email

        if not isinstance(client_phone_number, str) or not client_phone_number.strip():
            raise ValueError("Client phone number must be a non-empty string.")
        self.__client_phone_number: str = client_phone_number

    def GetClientId(self) -> int:
        return self.__client_id

    def GetClientName(self) -> str:
        return self.__client_name

    def GetClientEmail(self) -> str:
        return self.__client_email

    def GetClientPhoneNumber(self) -> str:
        return self.__client_phone_number

    def SetClientId(self, client_id: int) -> None:
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Client ID must be a positive integer.")
        self.__client_id = client_id

    def SetClientName(self, client_name: str) -> None:
        if not isinstance(client_name, str) or not client_name.strip():
            raise ValueError("Client name must be a non-empty string.")
        self.__client_name = client_name

    def SetClientEmail(self, client_email: str) -> None:
        if not isinstance(client_email, str) or not client_email.strip():
            raise ValueError("Client email must be a non-empty string.")
        self.__client_email = client_email

    def SetClientPhoneNumber(self, client_phone_number: str) -> None:
        if not isinstance(client_phone_number, str) or not client_phone_number.strip():
            raise ValueError("Client phone number must be a non-empty string.")
        self.__client_phone_number = client_phone_number