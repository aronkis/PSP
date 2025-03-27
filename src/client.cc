#include "../include/client.h"
#include "../include/message.h"

#include <sstream>

std::string Client::GetResponse(std::string command)
{

    std::string response;
    this->ConnectToServer();
    this->SendMessage(Message(id_, command, connection_.GetTodaysDate()));
    this->ReceiveMessage(&response);

    return response;
}

void Client::ConnectToServer() {
    connection_.CreateSocket();
    connection_.ConnectToServer();
}

void Client::SendMessage(const Message& message) {
    connection_.SendData(message);
}

void Client::ReceiveMessage(std::string* response) {
    connection_.ReceiveData(response);
}

Hotel ParseHotelData(const std::string& sqlResponse) {
    int id;
    std::string name;
    std::string location;

    // Parse the SQL response string
    std::istringstream stream(sqlResponse);
    std::string token;

    while (stream >> token) {
        if (token == "id:") {
            stream >> id;
        } else if (token == "name:") {
            std::getline(stream, name, ' '); 
            name = name.substr(0, name.size() - 1);
        } else if (token == "location:") {
            std::getline(stream, location);
        }
    }

    return Hotel(id, name, location);
}

std::vector<Room> Client::FilterRooms(const std::string &hotel_name, const std::string &location,
                                      bool availability, double max_price,
                                      const std::vector<std::string> &required_facilities)
{
    Hotel hotel = Hotel(hotel_name);
    std::vector<Room> rooms = hotel.GetRooms();
    return hotel.FilterRooms(location, availability, max_price, required_facilities);
}