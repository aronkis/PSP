#include "../include/user.h"
#include <sstream>
#include <format>
#include <iostream>

void User::Login()
{
    std::string command = std::format(
                            "SELECT username FROM Users WHERE username = '{}' AND password = '{}'",
                            GetUsername(), GetPassword());
    std::string response = GetResponse(command);
    std::istringstream stream(response);

    stream.ignore(std::numeric_limits<std::streamsize>::max(), ' ');    
    std::string username;
    stream >> username;
    
    if (username == username_)
    {
        logged_in_ = true;
    }
    else
    {
        logged_in_ = false;
        throw std::invalid_argument("Wrong username or password\n");
    }
}

void User::ConnectToServer()
{
    connection_.CreateSocket();
    connection_.ConnectToServer();
}

void User::SendMessage(const Message &message)
{
    connection_.SendData(message);
}

void User::ReceiveMessage(std::string *response)
{
    connection_.ReceiveData(response);
}

std::string User::GetResponse(std::string command)
{

    std::string response;
    ConnectToServer();
    SendMessage(Message(id_, command, connection_.GetTodaysDate()));
    ReceiveMessage(&response);

    return response;
}
