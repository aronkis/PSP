#ifndef ROOM_H
#define ROOM_H

#include <string>
#include <vector>

class Room {
public:
    Room(int id, const std::string& location, int number, bool is_available, 
         double price, const std::vector<std::string>& facilities) :
         id_(id), location_(location), number_(number), is_available_(is_available),
         price_(price), facilities_(facilities) {};
    
    int GetId() const { return id_; }
    int GetNumber() const { return number_; }
    bool GetAvailability() const { return is_available_; }
    double GetPrice() const { return price_; }
    std::string GetLocation() const { return location_; }
    std::vector<std::string> GetFacilities() const { return facilities_; }

    void SetAvailability(bool availability) { is_available_ = availability; }
    void SetPrice(double price) { this->price_ = price; }
    void SetFacilities(const std::vector<std::string>& facilities) { this->facilities_ = facilities; }

    bool MatchesFilter(const std::string& location, bool availability,
        double max_price, const std::vector<std::string>& required_facilities) const;

private:
    int id_;
    int number_;
    std::string location_;
    double price_;
    bool is_available_;
    std::vector<std::string> facilities_;
};

#endif
