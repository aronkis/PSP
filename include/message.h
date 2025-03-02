#ifndef _CLIENTSERVER_MESSAGE_H_
#define _CLIENTSERVER_MESSAGE_H_

#include <string>
#include <boost/serialization/base_object.hpp>

class Message
{
public:
	Message() = default;
	Message(int sender, std::string text, std::string date)
		: text_(text), sender_(sender), date_(date) {}
	inline std::string getText() { return text_; }
	inline int getSender() { return sender_; }
	inline std::string getDate() { return date_; }

	friend class boost::serialization::access;
	template <class Archive>
	void serialize(Archive &ar, const unsigned int version)
	{
		ar & text_;
		ar & sender_;
		ar & date_;
	}

private:
	int sender_;
	std::string text_;
	std::string date_;
};

#endif