#include "include/UpdateRoomDialog.h"
#include <iostream>
#include <QMessageBox>
#include "../include/employee.h"
#include "../include/room.h"

UpdateRoomDialog::UpdateRoomDialog(QWidget *parent) : QDialog(parent)
{
    // Create the widgets
    hotelNameLineEdit = new QLineEdit(this);
    roomNumberLineEdit = new QLineEdit(this);
    priceLineEdit = new QLineEdit(this);
    roomAvailableComboBox = new QComboBox(this);
    facilitiesLineEdit = new QLineEdit(this);
    updateRoomButton = new QPushButton("Update Room", this);
    cancelButton = new QPushButton("Cancel", this);

    // Set up the room type combo box with some example room types
    roomAvailableComboBox->addItem("Yes");
    roomAvailableComboBox->addItem("No");

    // Layout setup
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    // Hotel Name
    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotelNameLineEdit);
    mainLayout->addLayout(hotelNameLayout);

    // Room Number
    QHBoxLayout *roomNumberLayout = new QHBoxLayout();
    roomNumberLayout->addWidget(new QLabel("Room Number:", this));
    roomNumberLayout->addWidget(roomNumberLineEdit);
    mainLayout->addLayout(roomNumberLayout);

    // Price
    QHBoxLayout *priceLayout = new QHBoxLayout();
    priceLayout->addWidget(new QLabel("Price:", this));
    priceLayout->addWidget(priceLineEdit);
    mainLayout->addLayout(priceLayout);

    // Room Available
    QHBoxLayout *roomTypeLayout = new QHBoxLayout();
    roomTypeLayout->addWidget(new QLabel("Available:", this));
    roomTypeLayout->addWidget(roomAvailableComboBox);
    mainLayout->addLayout(roomTypeLayout);

    // Facilities
    QHBoxLayout *facilitiesLayout = new QHBoxLayout();
    facilitiesLayout->addWidget(new QLabel("Facilities:", this));
    facilitiesLayout->addWidget(facilitiesLineEdit);
    mainLayout->addLayout(facilitiesLayout);

    // Buttons
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(updateRoomButton);
    buttonLayout->addWidget(cancelButton);
    mainLayout->addLayout(buttonLayout);

    // Connect signals and slots
    connect(updateRoomButton, &QPushButton::clicked, this, &UpdateRoomDialog::onUpdateRoomButtonClicked);
    connect(cancelButton, &QPushButton::clicked, this, &UpdateRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Update Room");
}

UpdateRoomDialog::~UpdateRoomDialog()
{
    // Cleanup if necessary (currently handled by Qt's parent-child system)
}

void UpdateRoomDialog::onUpdateRoomButtonClicked()
{
    // Validate inputs
    bool valid = true;
    QString hotelName = hotelNameLineEdit->text();
    QString roomNumber = roomNumberLineEdit->text();
    QString roomAvailable = roomAvailableComboBox->currentText();
    QString priceText = priceLineEdit->text();
    double price;
    QString facilities = facilitiesLineEdit->text();

    if (hotelName.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Hotel name cannot be empty!");
        valid = false;
    }

    if (roomNumber.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Room number cannot be empty!");
        valid = false;
    }

    Employee e = Employee(2, "employee1", "employee1@example.com", "password123");
 
    bool is_available = roomAvailable == "Yes" ? 1 : 0;

    try
    {
        Room r = e.ReadRoom(hotelName.toStdString(), roomNumber.toInt());
        
        if (priceText.isEmpty()) {
            price = r.GetPrice();
        }
        else
        {
            price = priceText.toDouble();
        }

        QStringList facilitiesList;
        std::vector<std::string> room_facilities;

        if (facilities.isEmpty())
        {
            room_facilities = r.GetFacilities();
        }
        else
        {
            facilitiesList = facilities.split(",");
            for (const auto &facility : facilitiesList) {
                room_facilities.push_back(facility.toStdString());
            }
        }
        
        int id = r.GetId();
        std::string floor = r.GetLocation();
        
        Room room = Room(id, floor, roomNumber.toInt(), is_available , price, room_facilities);

        e.UpdateRoom(hotelName.toStdString(), roomNumber.toInt(), room);

        QMessageBox::information(this, "Room Created", "The room has been created successfully!");
        accept();
    }
    catch(const std::exception& e)
    {
        QMessageBox::information(this, "Invalid Input", e.what());
    }
}