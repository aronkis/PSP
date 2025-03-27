#include "../include/employee.h"
#include "../include/room.h"

#include <iostream>

int main()
{
    try
    {
        Employee e = Employee(2, "employee1", "employee1@example.com", "password123");
        std::string hotel_name = "Grand Hotel";
        int room_number = 999;
        std::vector<std::string> room_facilities = {"WiFi", "AC"};
        Room room = Room(99, "Floor 8", room_number, 1, 789.0, room_facilities);

        e.CreateRoom(hotel_name, room);
        Room r = e.ReadRoom(hotel_name, room_number);
        std::cout << "Room added with details: id = " << r.GetId() << " location = "
                  << r.GetLocation() << " number = " << r.GetNumber() << " price = "
                  << r.GetPrice() << " facilities = ";
        for (const auto &facility : r.GetFacilities())
        {
            std::cout << facility << " ";
        }
        std::cout << "\n";

        room = e.ReadRoom(hotel_name, room_number);
        room.SetPrice(25.0);
        e.UpdateRoom(hotel_name, room_number, room);
        r = e.ReadRoom(hotel_name, room_number);
        std::cout << "Room updated with details: id = " << r.GetId() << " location = "
                  << r.GetLocation() << " number = " << r.GetNumber() << " price = "
                  << r.GetPrice() << " facilities = ";
        for (const auto &facility : r.GetFacilities())
        {
            std::cout << facility << " ";
        }
        std::cout << "\n";

        e.DeleteRoom(hotel_name, room_number);

        try
        {
            r = e.ReadRoom(hotel_name, room_number);
            std::cout << "Room not deleted with details: id = " << r.GetId() << " location = "
                      << r.GetLocation() << " number = " << r.GetNumber() << " price = "
                      << r.GetPrice() << " facilities = ";
            for (const auto &facility : r.GetFacilities())
            {
                std::cout << facility << " ";
            }
            std::cout << "\n";
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << '\n';
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
    }
}