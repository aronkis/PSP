#include "include/ClientGUI.h"
#include "ui/ClientUI/ui_ClientGUI.h"
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QDebug>
#include "../include/client.h"
#include "../include/room.h"

ClientGUI::ClientGUI(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::ClientGUI)
{
    ui->setupUi(this);

    connect(ui->sendButton, &QPushButton::clicked, this, &ClientGUI::OnSendButtonClicked);
}

ClientGUI::~ClientGUI()
{
    delete ui;
}

void ClientGUI::OnSendButtonClicked()
{
    QString hotel_name = ui->hotelName->text();
    QString roomLocation = ui->roomLocationInput->text();
    QString roomPrice = ui->roomPriceInput->text();
    QString roomAvailability = ui->roomAvailabilityInput->text();
    QString roomFacilities = ui->roomFacilitiesInput->text();

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

        ui->roomIdLabel->setText(id_label);
        ui->roomNumberLabel->setText(number_label);
        ui->roomLocationLabel->setText(location_label);
        ui->roomPriceLabel->setText(price_label);
        ui->roomAvailabilityLabel->setText(availability_label);
        
        QStringList outputFacilities;
        for (const auto& facility : room.GetFacilities()) {
            outputFacilities << QString::fromStdString(facility);
        }
        ui->roomFacilitiesLabel->setText("Facilities: " + outputFacilities.join(" "));
    }
    else
    {
        ui->roomIdLabel->setText("Room ID: No rooms available");
        ui->roomNumberLabel->setText("Number: N/A");
        ui->roomLocationLabel->setText("Location: N/A");
        ui->roomPriceLabel->setText("Price: N/A");
        ui->roomAvailabilityLabel->setText("Available: N/A");
        ui->roomFacilitiesLabel->setText("Facilities: N/A");
    }
}
