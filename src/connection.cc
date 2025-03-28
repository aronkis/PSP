#include <chrono>
#include <sstream>
#include <arpa/inet.h>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>

#include "../include/message.h"
#include "../include/connection.h"

void Connection::CreateSocket()
{
	socket_info_ = socket(AF_INET, SOCK_STREAM, 0);

	if (socket_info_ < 0)
	{
		perror("ERROR WHILE OPENING THE SOCKET\n");
		exit(EXIT_FAILURE);
	}

	server_addr_.sin_family = AF_INET;
	server_addr_.sin_port = htons(8080);

	if (inet_pton(AF_INET, "127.0.0.1", &server_addr_.sin_addr) <= 0)
	{
		perror("INET_PTON FAILED!\n");
		exit(EXIT_FAILURE);
	}
}

void Connection::ConnectToServer()
{
	if (connect(socket_info_, (struct sockaddr *)&server_addr_, 
				sizeof(server_addr_)) < 0)
	{
		perror("ERROR WHILE CONNECTING!\n");
		exit(EXIT_FAILURE);
	}
}

void Connection::ReceiveData(std::string* response)
{

    char buffer[50000];
    int bytes_received = read(socket_info_, buffer, sizeof(buffer));
    if (bytes_received < 0)
    {
        perror("ERROR WHILE RECEIVING RESPONSE FROM SERVER!\n");
        exit(EXIT_FAILURE);
    }
    std::string serialized_msg(buffer, bytes_received);
    Message response_message;
    std::stringstream ss(serialized_msg);
    boost::archive::text_iarchive ia(ss);
    ia >> response_message;

	*response = response_message.GetText();
}

void Connection::SendData(const Message message)
{
	std::stringstream ss;
	boost::archive::text_oarchive oa(ss);
	oa << message;
	std::string serialized_msg = ss.str();

	if (send(socket_info_, serialized_msg.c_str(), 
		serialized_msg.size(), 0) < 0)
	{
		throw std::runtime_error("Error sending message from user");
	}
}

std::string Connection::GetTodaysDate() {
    auto now = std::chrono::system_clock::now();
    
    std::time_t now_c = std::chrono::system_clock::to_time_t(now);
    
    std::tm now_tm = *std::localtime(&now_c);
    
    std::ostringstream oss;
    oss << std::put_time(&now_tm, "%Y-%m-%d");

    return oss.str();
}