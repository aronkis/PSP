#include "../include/client.h"
#include "../include/message.h"

#include <cstring>
#include <iostream>

void Client::ShowListOfRooms(const char* hotel_name)
{
    char command[255] = "SELECT room_number, floor_number, price_per_night, room_type FROM ";
    std::strcat(command, hotel_name);
    std::strcat(command, ";");

    SendData(Message(this->GetClientId(), command, "2025-03-02"));
}