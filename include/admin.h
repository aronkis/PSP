#ifndef ADMIN_H
#define ADMIN_H

#include "user.h"

class Admin : public User {
public:
    Admin(int id, const std::string& username, const std::string& email, 
          const std::string& password) : User(id, username, email, password) {}
};

#endif
