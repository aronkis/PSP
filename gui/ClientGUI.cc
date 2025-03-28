#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QDebug>

#include "include/ClientGUI.h"
#include "ui/ClientUI/ui_ClientGUI.h"

#include "../include/client.h"
#include "../include/room.h"

ClientGUI::ClientGUI(QWidget *parent)
    : QMainWindow(parent), ui_(new Ui::ClientGUI)
{
    ui_->setupUi(this);

    connect(ui_->sendButton, &QPushButton::clicked, this, &ClientGUI::OnSendButtonClicked);
}

ClientGUI::~ClientGUI()
{
    delete ui_;
}

void ClientGUI::OnSendButtonClicked()
{
    QString hotel_name = ui_->hotelNameInput->text();
    QString roomLocation = ui_->roomLocationInput->text();
    QString roomPrice = ui_->roomPriceInput->text();
    QString roomAvailability = ui_->roomAvailabilityInput->text();
    QString roomFacilities = ui_->roomFacilitiesInput->text();

    if (hotel_name.isEmpty() || roomLocation.isEmpty() || roomPrice.isEmpty() || 
        roomAvailability.isEmpty() || roomFacilities.isEmpty()) 
    {
        qDebug() << "Please complete all input fields.";
        return;
    }

    bool priceOk;
    double price = roomPrice.toDouble(&priceOk);
    if (!priceOk) {
        qDebug() << "Invalid price!";
        return;
    }

    if (roomAvailability != "Yes" && roomAvailability != "No") {
        qDebug() << "Invalid availability input!";
        return;
    }

    QStringList facilitiesList = roomFacilities.split(",");

    Client c(1, "john", "john@example.com", "12398123");
    std::vector<std::string> required_facilities;
    for (const auto &facility : facilitiesList) {
        required_facilities.push_back(facility.toStdString());
    }
    bool is_available = roomAvailability == "Yes" ? 1 : 0;
    std::vector<Room> rooms = c.FilterRooms(hotel_name.toStdString(), roomLocation.toStdString(), 
                                            is_available, price, required_facilities);

    if (!rooms.empty())
    {
        const Room& room = rooms[0];

        QString id_label = "Room ID: " + QString::number(room.GetId());
        QString number_label = "Number: " + QString::number(room.GetNumber());
        QString location_label = "Location: " + QString::fromStdString(room.GetLocation());
        QString price_label = "Price: " + QString::number(room.GetPrice());
        QString availability_label = "Available: " + QString::fromStdString(room.GetAvailability() ? "Yes" : "No");

        for (size_t i = 1; i < rooms.size(); ++i) {
            const Room& room = rooms[i];
            id_label += ", " + QString::number(room.GetId());
            number_label += ", " + QString::number(room.GetNumber());
            location_label += ", " + QString::fromStdString(room.GetLocation());
            price_label += ", " + QString::number(room.GetPrice());
            availability_label += ", " + QString::fromStdString(room.GetAvailability() ? "Yes" : "No");
        }

        ui_->room_id_label_->setText(id_label);
        ui_->room_number_label_->setText(number_label);
        ui_->room_location_label->setText(location_label);
        ui_->room_price_label->setText(price_label);
        ui_->room_availability_label_->setText(availability_label);
        
        QStringList outputFacilities;
        for (const auto& facility : room.GetFacilities()) {
            outputFacilities << QString::fromStdString(facility);
        }
        ui_->room_facilities_label_->setText("Facilities: " + outputFacilities.join(" "));
    }
    else
    {
        ui_->room_id_label_->setText("Room ID: No rooms available");
        ui_->room_number_label_->setText("Number: N/A");
        ui_->room_location_label->setText("Location: N/A");
        ui_->room_price_label->setText("Price: N/A");
        ui_->room_availability_label_->setText("Available: N/A");
        ui_->room_facilities_label_->setText("Facilities: N/A");
    }
}
