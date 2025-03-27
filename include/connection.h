#ifndef CONNECTION_H
#define CONNECTION_H

#include <netinet/in.h>
#include <string>
#include "message.h"

class Connection {

public:
	void CreateSocket();
	void ConnectToServer();
	void SendData(const Message message);
	void ReceiveData(std::string* response);
	std::string GetTodaysDate();

protected:
	int socket_info_ = 0;
	struct sockaddr_in server_addr_;
};

#endif

