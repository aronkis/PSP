#include "../include/room.h"
#include <algorithm>

bool Room::MatchesFilter(const std::string& location, bool availability, double max_price, 
                         const std::vector<std::string>& required_facilities) const 
{
    bool matchesLocation = (location.empty() || location_ == location);
    bool matchesAvailability = (is_available_ == availability);
    bool matchesPrice = (price_ <= max_price);
    
    bool matchesFacilities = true;
    for (const auto& facility : required_facilities) {
        if (std::find(facilities_.begin(), facilities_.end(), facility) == facilities_.end()) {
            matchesFacilities = false;
            break;
        }
    }
    
    return matchesLocation && matchesAvailability && matchesPrice && matchesFacilities;
}
