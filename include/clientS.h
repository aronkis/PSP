#ifndef _CLIENTSERVER_CLIENTS_H_
#define _CLIENTSERVER_CLIENTS_H_

#include <netinet/in.h>
#include "message.h"

class ClientS
{
public:
	ClientS(int client_id, int client_type) : client_type_(client_type), 
											  client_id_(client_id) {}
	int GetClientType() { return client_type_; }
	int GetClientId() { return client_id_; }
	void CreateSocket();
	void ConnectToServer();
	void SendData(const Message message);
	void ReceiveData();

private:
	int client_type_;
	int client_id_;
	int socket_info_ = 0;
	struct sockaddr_in server_addr_;
};

#endif
