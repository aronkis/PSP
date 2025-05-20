from Domain.Client import Client

class IClientRepository:
    def CreateClient(self, client: Client) -> None:
        pass

    def UpdateClient(self, old_client_id: int, client: Client) -> None:
        pass

    def DeleteClient(self, client_id: int) -> None:
        pass

    def ListClients(self) -> dict:
        pass