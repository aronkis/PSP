#include "./include/server.h"
#include <iostream>

int main()
{
	Server server(8080);
	server.ConnectToSQL("../Hotels.db");
	server.CreateSocket();
	server.BindServer();
	server.ListenServer();
	server.AcceptClients();
}