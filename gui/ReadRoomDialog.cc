#include "include/ReadRoomDialog.h"
#include <iostream>
#include <QMessageBox>
#include "../include/employee.h"
#include "../include/room.h"

ReadRoomDialog::ReadRoomDialog(QWidget *parent) 
    : QDialog(parent)
{
    // Create the widgets
    hotelNameLineEdit = new QLineEdit(this);
    roomNumberLineEdit = new QLineEdit(this);

    readRoomButton = new QPushButton("Read Room", this);
    cancelButton = new QPushButton("Cancel", this);

    roomIdLabel = new QLabel("Room ID: N/A", this);
    roomNumberLabel = new QLabel("Number: N/A", this);
    roomLocationLabel = new QLabel("Location: N/A", this);
    roomPriceLabel = new QLabel("Price: N/A", this);
    roomAvailabilityLabel = new QLabel("Available: N/A", this);
    roomFacilitiesLabel = new QLabel("Facilities: N/A", this);

    // Layout setup
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    // Hotel Name Input
    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotelNameLineEdit);
    mainLayout->addLayout(hotelNameLayout);

    // Room Number Input
    QHBoxLayout *roomNumberLayout = new QHBoxLayout();
    roomNumberLayout->addWidget(new QLabel("Room Number:", this));
    roomNumberLayout->addWidget(roomNumberLineEdit);
    mainLayout->addLayout(roomNumberLayout);

    // Output Fields
    mainLayout->addWidget(roomIdLabel);
    mainLayout->addWidget(roomNumberLabel);
    mainLayout->addWidget(roomLocationLabel);
    mainLayout->addWidget(roomPriceLabel);
    mainLayout->addWidget(roomAvailabilityLabel);
    mainLayout->addWidget(roomFacilitiesLabel);

    // Buttons
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(readRoomButton);
    buttonLayout->addWidget(cancelButton);
    mainLayout->addLayout(buttonLayout);

    // Connect signals and slots
    connect(readRoomButton, &QPushButton::clicked, this, &ReadRoomDialog::onReadRoomClicked);
    connect(cancelButton, &QPushButton::clicked, this, &QDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Read Room");
}

ReadRoomDialog::~ReadRoomDialog()
{
    // Cleanup (handled by Qt's parent-child system)
}

void ReadRoomDialog::onReadRoomClicked()
{
    QString hotelName = hotelNameLineEdit->text();
    QString roomNumber = roomNumberLineEdit->text();

    if (hotelName.isEmpty() || roomNumber.isEmpty()) 
    {
        QMessageBox::warning(this, "Input Error", "Please complete all input fields.");
        return;
    }

    // Assume Employee has a method to fetch room by hotel name and room number
    Employee e = Employee(2, "employee1", "employee1@example.com", "password123");
    try
    {
        Room room = e.ReadRoom(hotelName.toStdString(), roomNumber.toInt());
        
        roomIdLabel->setText("Room ID: " + QString::number(room.GetId()));
        roomNumberLabel->setText("Number: " + QString::number(room.GetNumber()));
        roomLocationLabel->setText("Location: " + QString::fromStdString(room.GetLocation()));
        roomPriceLabel->setText("Price: " + QString::number(room.GetPrice()));
        roomAvailabilityLabel->setText("Available: " + QString::fromStdString(room.GetAvailability() ? "Yes" : "No"));

        QStringList outputFacilities;
        for (const auto& facility : room.GetFacilities()) {
            outputFacilities << QString::fromStdString(facility);
        }
        roomFacilitiesLabel->setText("Facilities: " + outputFacilities.join(" "));
    }
    catch(const std::exception& e)
    {
        roomIdLabel->setText("Room ID: No rooms available");
        roomNumberLabel->setText("Number: N/A");
        roomLocationLabel->setText("Location: N/A");
        roomPriceLabel->setText("Price: N/A");
        roomAvailabilityLabel->setText("Available: N/A");
        roomFacilitiesLabel->setText("Facilities: N/A");
        std::cerr << e.what() << '\n';
    }
    

    
}

