#include "../include/hotel.h"
#include <sstream>

Hotel::Hotel(std::string hotel_name)
{
    id_ = 9999;
    std::string response = GetResponse(std::format("SELECT * FROM hotels WHERE name = '{}'", hotel_name));
    int id;
    std::string name;
    std::string location;

    std::istringstream stream(response);
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

    id_ = id;
    name_ = name;
    location_ = location;
    FillRooms();
}

Room Hotel::GetRoom(int number)
{
    for (const auto& room : rooms_) {
        if (room.GetNumber() == number) {
            return room;
        }
    }
    throw std::runtime_error("Room with number " + std::to_string(number) + " not found.");
}

std::string GetFacilities(Room room)
{
    std::vector<std::string> facilities = room.GetFacilities();
    std::string facilities_string = facilities[0];
    for (size_t i = 1; i < facilities.size(); ++i) 
    {
        facilities_string += ", " + facilities[i];
    }
    return facilities_string;
}

void Hotel::CreateRoom(const Room& room) 
{
    rooms_.push_back(room);

    std::string facilities = GetFacilities(room);
    std::string command = std::format(
        "INSERT INTO rooms (id, hotel_id, number, location, price, available, facilities) VALUES ({}, {}, {}, '{}', {}, {}, '{}')", 
        room.GetId(), id_, room.GetNumber(), room.GetLocation(), room.GetPrice(),
        room.GetAvailability(), facilities);
    GetResponse(command);
}

void Hotel::UpdateRoom(int number, const Room& room) 
{
    for (auto& room : rooms_) {
        if (room.GetNumber() == number) {
            room = room;
            break;
        }
    }
    std::string facilities = GetFacilities(room);
    std::string command = std::format(
        "UPDATE Rooms SET price = {}, available = {}, facilities = '{}' WHERE id = {}",
        room.GetPrice(), room.GetAvailability(), facilities, room.GetId());
    GetResponse(command);
}

void Hotel::DeleteRoom(int number) 
{
    rooms_.erase(std::remove_if(rooms_.begin(), rooms_.end(), 
                                [number](const Room& room) { 
                                                            return room.GetNumber() == number; 
                                                       }
                                ), rooms_.end()
                );
    std::string command = std::format("DELETE FROM rooms WHERE number = {}", number);
    GetResponse(command);
}

std::vector<Room> Hotel::GetAvailableRooms() 
{
    std::vector<Room> rooms;
    for (const auto& room: GetRooms())
    {
        if (room.GetAvailability())
        {
            rooms.push_back(room);
        }
    }
    return rooms;
}

std::vector<Room> Hotel::FilterRooms(const std::string& location, bool availability, double max_price,
                                     const std::vector<std::string>& required_facilities) const 
{
    std::vector<Room> filteredRooms;
        
    for (const auto& room : rooms_) {
        if (room.MatchesFilter(location, availability, max_price, required_facilities)) {
            filteredRooms.push_back(room);
        }
    }

    return filteredRooms;
}

std::string Hotel::GetResponse(std::string command)
{

    std::string response;
    ConnectToServer();
    SendMessage(Message(id_, command, connection_.GetTodaysDate()));
    ReceiveMessage(&response);

    return response;
}

void Hotel::ConnectToServer() {
    connection_.CreateSocket();
    connection_.ConnectToServer();
}

void Hotel::SendMessage(const Message& message) {
    connection_.SendData(message);
}

void Hotel::ReceiveMessage(std::string* response) {
    connection_.ReceiveData(response);
}

std::vector<std::string> ParseFacilities(const std::string& facilities_string) {
    std::vector<std::string> facilities;
    std::istringstream stream(facilities_string);
    std::string facility;

    while (std::getline(stream, facility, ',')) {
        // Remove leading and trailing whitespace
        facility.erase(0, facility.find_first_not_of(" \t"));
        facility.erase(facility.find_last_not_of(" \t") + 1);
        facilities.push_back(facility);
    }

    return facilities;
}

Room ParseRoomData(const std::string& response) {
    int id, hotel_id, number;
    std::string location, facilities_string;
    double price = 0.0;
    bool available;

    std::istringstream stream(response);
    std::string token;

    while (stream >> token) {
        if (token == "id:") {
            stream >> id;
        } else if (token == "hotel_id:") {
            stream >> hotel_id;
        } else if (token == "number:") {
            stream >> number;
        } else if (token == "location:") {
            std::getline(stream, location, 'p');
            location = location.substr(0, location.size() - 1).substr(1);
        } else if (token == "rice:") {
            stream >> price;
        } else if (token == "available:") {
            int availableInt;
            stream >> availableInt;
            available = (availableInt == 1);
        } else if (token == "facilities:") {
            std::getline(stream, facilities_string);
            facilities_string.erase(0, facilities_string.find_first_not_of(" \t")); // Remove leading whitespace
        }
    }

    std::vector<std::string> facilities = ParseFacilities(facilities_string);
    return Room(id, location, number, available, price, facilities);
}

std::vector<Room> ParseRoomsData(const std::string& response) {
    std::vector<Room> rooms;
    std::istringstream stream(response);
    std::string line;

    while (std::getline(stream, line)) {
        if (!line.empty()) {
            rooms.push_back(ParseRoomData(line));
        }
    }

    return rooms;
}

void Hotel::FillRooms()
{
    std::string response = GetResponse(std::format("SELECT * FROM rooms WHERE hotel_id = '{}'", id_));
    rooms_ = ParseRoomsData(response);
}
