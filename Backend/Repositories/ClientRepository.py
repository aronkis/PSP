from Domain.IClientRepository import IClientRepository
from Repositories.Repository import Repository
from Domain.Client import Client
import json

class ClientRepository(IClientRepository):
    def __init__ (self):
        self.__client_repository: Repository = Repository()

    def CreateClient(self, client: Client) -> None:
        if not isinstance(client, Client):
            raise ValueError("Expected a Client object.")
        self.__client_repository.ModifyData(""" INSERT INTO Client (id, client_name, client_email, client_phone_number) VALUES (?, ?, ?, ?) """, \
                       (client.GetClientId(), client.GetClientName(), client.GetClientEmail(), client.GetClientPhoneNumber()))
    
    def UpdateClient(self, old_client_id: int, client: Client) -> None:
        if not isinstance(client, Client):
            raise ValueError("Expected a Client object.")
        if not isinstance(old_client_id, int):
            raise ValueError("Expected the old client id to be an int.")
        self.__client_repository.ModifyData("""
            UPDATE Client SET id = ?, client_name = ?, client_email = ?, client_phone_number = ?
            WHERE id=?""", (client.GetClientId(), client.GetClientName(), client.GetClientEmail(), client.GetClientPhoneNumber(), old_client_id))

    def DeleteClient(self, client_id: int) -> None:
        if not isinstance(client_id, int):
            raise ValueError("Expected the client id to be an int.")
        self.__client_repository.ModifyData("DELETE FROM Client WHERE id=?", (client_id, ))

    def ListClients(self) -> dict:
        data:str = self.__client_repository.GetData("SELECT * FROM Client")
        return json.loads(data)
