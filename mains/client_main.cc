#include "../include/client.h"
#include "../include/room.h"

#include <iostream>

int main()
{
	Client c = Client(1, "john", "john@example.com", "12398123");
	std::string hotel_name = "Grand Hotel";
	std::vector<std::string> required_facilities = {"WiFi"};
	
	std::vector<Room> rooms = c.FilterRooms(hotel_name, "Floor 1", 1, 170.0, required_facilities);
    std::cout << "Hotel: " << hotel_name << "\n";
	for (const auto &room : rooms)
    {
        std::cout << "Room ID: " << room.GetId() << ", Number: " << room.GetNumber()
                  << ", Location: " << room.GetLocation() << ", Price: " << room.GetPrice()
                  << ", Available: " << (room.GetAvailability() ? "Yes" : "No") << ", Facilities: ";
        for (const auto &facility : room.GetFacilities())
        {
            std::cout << facility << " ";
        }
        std::cout << std::endl;
    }

}