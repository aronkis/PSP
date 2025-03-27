#include "../include/employee.h"

Room Employee::ReadRoom(std::string hotel_name, int room_number)
{
    Hotel hotel = Hotel(hotel_name);
    return hotel.GetRoom(room_number);
}

void Employee::CreateRoom(std::string hotel_name, Room room)
{
    Hotel hotel = Hotel(hotel_name);
    hotel.CreateRoom(room);
}

void Employee::UpdateRoom(std::string hotel_name, int room_number, Room room)
{
    Hotel hotel = Hotel(hotel_name);
    hotel.UpdateRoom(room_number, room);
}

void Employee::DeleteRoom(std::string hotel_name, int room_number)
{
    Hotel hotel = Hotel(hotel_name);
    hotel.DeleteRoom(room_number);
}

