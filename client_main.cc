#include "./include/clientS.h"
#include "./include/client.h"
#include "./include/message.h"

void clientAskData(const char* name, Client client)
{
	client.CreateSocket();
	client.ConnectToServer();
	client.ShowListOfRooms(name);
}

int main()
{
	Client client(1);
	clientAskData("grand_plaza", client);
	// clientAskData("Seaside Resort", client);
	// clientAskData("Mountain View Inn", client);
	// clientAskData("Lakeside Hotel", client);
	// clientAskData("City Center Hotel", client);
	
}