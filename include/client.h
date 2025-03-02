#ifndef _CLIENTSERVER_CLIENT_H_
#define _CLIENTSERVER_CLIENT_H_
// Vizualizarea listei camerelor dintr-un hotel selectat sortată după locație și număr;
// Filtrarea listei camerelor după locație, disponibilitate, preț, poziție, facilități. 
#include "clientS.h"
#include <string>

class Client : public ClientS
{
public:
    Client(int client_id, int client_type = 0) : ClientS(client_id, client_type){}
    void ShowListOfRooms(const char* hotel_name); // sorting done viq querry
    void FilterRooms(std::string location, int disponibility, 
                     float price, std::string position, std::string facilities);
};

#endif
