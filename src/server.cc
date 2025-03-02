#include <sstream>
#include <boost/serialization/string.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>
#include "../include/server.h"
#include "../include/message.h"
#include <iostream>

std::ofstream Server::log_("../logs.txt", std::fstream::out | std::fstream::app);
sqlite3* Server::db = nullptr;

Server::~Server()
{
	if (new_socket_ != 0)
	{
		close(new_socket_);
	}
	if (server_info_ != 0)
	{
		close(server_info_);
	}
	sqlite3_close(db);
}

void Server::CreateSocket()
{
	if ((server_info_ = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		perror("ERROR WHILE OPENING THE SOCKET\n");
		exit(EXIT_FAILURE);
	}

	int opt = 1;
	if (setsockopt(server_info_, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
				   &opt, sizeof(opt)))
	{
		perror("ERROR WHILE SETTING THE OPTION!\n");
		exit(EXIT_FAILURE);
	}
}

void Server::BindServer()
{
	server_addr_.sin_family = AF_INET;
	server_addr_.sin_addr.s_addr = INADDR_ANY;
	server_addr_.sin_port = htons(port_);
	if (bind(server_info_, (struct sockaddr *)&server_addr_, sizeof(server_addr_)) < 0)
	{
		perror("ERROR WHILE BIDING!\n");
		exit(EXIT_FAILURE);
	}
}

void Server::ListenServer()
{
	if (listen(server_info_, 5) < 0)
	{
		perror("ERROR WHILE LISTENING!\n");
		exit(EXIT_FAILURE);
	}
}

void Server::SendResponse(int socket, const Message& message)
{

    std::stringstream ss;
    boost::archive::text_oarchive oa(ss);
    oa << message;  
    std::string serialized_msg = ss.str();  

    if (send(socket, serialized_msg.c_str(), serialized_msg.size(), 0) < 0)
    {
        perror("ERROR WHILE SENDING RESPONSE TO CLIENT!\n");
        return;
    }
}

void Server::HandleClient(int socket)
{
	char buffer[1024];
	int bytes_received = read(socket, buffer, sizeof(buffer));
	if (bytes_received < 0)
	{
		perror("ERROR WHILE HANDLING A CLIENT!\n");
		exit(EXIT_FAILURE);
	}
	std::string serialized_msg(buffer, bytes_received);
	Message message;

	std::stringstream ss(serialized_msg);
	boost::archive::text_iarchive ia(ss);
	ia >> message;
	log_ <<"Client id: " << message.getSender() << " Date: " << message.getDate() << std::endl;
	
	Message sql_response;
	ExecuteSQLCommand(message.getText().c_str(), sql_response);
    SendResponse(socket, sql_response);
	
	Message response_message(100, "SQL command executed successfully!", "2025-03-02");
	log_ <<"Server id: " << response_message.getSender() << " " << response_message.getText() << " Date: " << response_message.getDate() << std::endl;
	close(socket);
}

void Server::AcceptClients()
{
	while (true)
	{
		int server_len = sizeof(server_addr_);
		new_socket_ = accept(server_info_, (struct sockaddr *)&server_addr_, (socklen_t *)&server_len);

		if (new_socket_ < 0)
		{
			perror("ERROR WHILE ACCEPTING A CLIENT!\n");
			exit(EXIT_FAILURE);
		}
		clients_.emplace_back(std::thread(Server::HandleClient, new_socket_));
	}
}

void Server::ConnectToSQL(const char* database)
{
    char* errMessage = 0;

    if (sqlite3_open(database, &db)) {
        log_ << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    } else {
        log_ << "Opened database successfully!" << std::endl;
    }
}

static int PrintQuerryData(void* data, int nr_of_columns, char** row_value, char** column_names) 
{
	std::string* response = static_cast<std::string*>(data);

    for (int i = 0; i < nr_of_columns; i++) {
        *response += column_names[i];
        *response += ": ";
        *response += (row_value[i] ? row_value[i] : "NULL");
        *response += " ";
    }
    *response += "\n";
    return 0;
}

void Server::ExecuteSQLCommand(const char* command, Message& message)
{
	char* errMessage = 0;
	std::string data;

	if (sqlite3_exec(db, command, 
		PrintQuerryData, &data, &errMessage) != SQLITE_OK) 
	{
		log_ << "SQL error (select): " << errMessage << std::endl;
		data = errMessage;
		sqlite3_free(errMessage);
	}

	if (data.length() == 0)
	{
		data = "No data found";
	}
	Message response_message(100, data, "2025-03-02");
	message = response_message;
}