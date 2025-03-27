#include "../include/user.h"
#include <sstream>
#include <format>

void User::Login()
{
    std::string command = std::format(
                            "SELECT id FROM Users WHERE username = '{}' AND password = '{}'",
                            GetUsername(), GetPassword());
    std::string response = GetResponse(command);
    std::istringstream stream(response);

    stream.ignore(std::numeric_limits<std::streamsize>::max(), ' ');    
    int id;
    stream >> id;
    
    if (id == id_)
    {
        logged_in_ = true;
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
