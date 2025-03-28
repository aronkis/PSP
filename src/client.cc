#include "../include/client.h"
#include "../include/message.h"

std::vector<Room> Client::FilterRooms(const std::string &hotel_name, const std::string &location,
                                      bool availability, double max_price,
                                      const std::vector<std::string> &required_facilities)
{
    Hotel hotel = Hotel(hotel_name);
    std::vector<Room> rooms = hotel.GetRooms();
    return hotel.FilterRooms(location, availability, max_price, required_facilities);
}