#ifndef HOTEL_H
#define HOTEL_H

#include <vector>
#include "connection.h"
#include "room.h"

class Hotel
{
public:
      Hotel (std::string hotel_name);
      Hotel(int id, const std::string &name, const std::string &location) 
              : id_(id), name_(name), location_(location) {}

      void CreateRoom(const Room &room);
      void UpdateRoom(int number, const Room &room);
      void DeleteRoom(int number);
      void FillRooms();

      Room GetRoom(int number);
      int GetId() { return id_; }
      std::vector<Room> GetAvailableRooms();
      std::vector<Room> GetRooms() const { return rooms_; }
      std::vector<Room> FilterRooms(const std::string &location, bool availability, double max_price,
                                    const std::vector<std::string> &required_facilities) const;

private:
      int id_;
      std::string name_;
      std::string location_;
      std::vector<Room> rooms_;
      Connection connection_;

      void ConnectToServer();
      void SendMessage(const Message &message);
      void ReceiveMessage(std::string *response);
      std::string GetResponse(std::string command);
};

#endif
