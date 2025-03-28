#ifndef CLIENT_H
#define CLIENT_H

#include <string>
#include "hotel.h"

class Client {
public:
    Client(int id, const std::string& name, const std::string& email, 
           const std::string& phone_number) : id_(id), name_(name), email_(email), 
                                              phone_number_(phone_number) {}
    
    int GetId() const { return id_; }
    std::string GetName() const { return name_; }
    std::string GetEmail() const { return email_; }

    void SetName(const std::string& name) { name_ = name; }
    void SetEmail(const std::string& email) { email_ = email; }

    std::vector<Room> FilterRooms(const std::string& hotel_name, const std::string& location, 
                                  bool availability, double max_price, 
                                  const std::vector<std::string>& required_facilities);

private:
    int id_;
    std::string name_;
    std::string email_;
    std::string phone_number_;
    std::vector<Room> booked_rooms_;
};

#endif
