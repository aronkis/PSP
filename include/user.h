#ifndef USER_H
#define USER_H

#include <netinet/in.h>
#include <string>
#include "message.h"
#include "connection.h"
#include <stdexcept>

class User {

public:

User(int id, const std::string& username, const std::string& email, 
	const std::string& password) : id_(id), username_(username), 
	email_(email), password_(password) 
	{
		Login();
		if (!logged_in_)
		{
			throw std::invalid_argument("Wrong username or password\n");
		}
	}

	virtual ~User() = default;

	virtual int GetId() const { return id_; }
	virtual std::string GetEmail() const { return email_; }
	virtual std::string GetUsername() const { return username_; }
	virtual std::string GetPassword() const { return password_; }

	virtual void SetId(int id) { id_ = id; }
	virtual void SetEmail(std::string email) {  email_ = email; }
	virtual void SetUsername(std::string username) {  username_ = username; }
	virtual void SetPassword(std::string password) {  password_ = password; }

	void Login();
	void Logout() { logged_in_ = false;  exit(0); }

protected:
    int id_;
	std::string email_;
    std::string username_;
	std::string password_;
	Connection connection_;
	bool logged_in_ = false;
	
	void ConnectToServer();
    void SendMessage(const Message& message);
    void ReceiveMessage(std::string* response);
	std::string GetResponse(std::string command);
};

#endif

