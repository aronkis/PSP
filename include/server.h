#ifndef _CLIENTSERVER_SERVER_H_
#define _CLIENTSERVER_SERVER_H_

#include <netinet/in.h>
#include <thread>
#include <vector>
#include <fstream>
#include <sqlite3.h>
#include "message.h"

class Server
{
public:
	Server(int port)
		: port_(port) {}
	~Server();
	void CreateSocket();
	void BindServer();
	void ListenServer();
	static void HandleClient(int socket);
	static void SendResponse(int socket, const Message& message);
	void AcceptClients();
	void ConnectToSQL(const char* database);
	static void ExecuteSQLCommand(const char* command, Message& message);

private:
	int port_ = 0;
	int server_info_ = 0, new_socket_ = 0;
	struct sockaddr_in server_addr_;
	static std::ofstream log_;
	std::vector<std::thread> clients_;
	static sqlite3* db;
};

#endif