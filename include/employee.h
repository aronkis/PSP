#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include "user.h"
#include "hotel.h"

class Employee : public User {
public:
    Employee(int id, const std::string& username, const std::string& email, 
            const std::string& password) : User(id, username, email, password) {}
    void CreateRoom(std::string hotel_name, Room room);
    Room ReadRoom(std::string hotel_name, int number);
    void UpdateRoom(std::string hotel_name, int room_number, Room room);
    void DeleteRoom(std::string hotel_name, int room_number);
};

#endif
