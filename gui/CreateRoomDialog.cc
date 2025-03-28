#include "include/CreateRoomDialog.h"
#include <iostream>
#include <QMessageBox>
#include "../include/employee.h"
#include "../include/room.h"

CreateRoomDialog::CreateRoomDialog(QWidget *parent) : QDialog(parent)
{
    // Create the widgets
    hotelNameLineEdit = new QLineEdit(this);
    roomFloorComboBox = new QComboBox(this);
    roomNumberLineEdit = new QLineEdit(this);
    priceLineEdit = new QLineEdit(this);
    roomAvailableComboBox = new QComboBox(this);
    facilitiesLineEdit = new QLineEdit(this);
    createRoomButton = new QPushButton("Create Room", this);
    cancelButton = new QPushButton("Cancel", this);

    // Set up the room type combo box with some example room types
    roomAvailableComboBox->addItem("Yes");
    roomAvailableComboBox->addItem("No");

    roomFloorComboBox->addItem("Floor 1");
    roomFloorComboBox->addItem("Floor 2");
    roomFloorComboBox->addItem("Floor 3");
    roomFloorComboBox->addItem("Floor 4");
    roomFloorComboBox->addItem("Floor 5");
    roomFloorComboBox->addItem("Floor 6");
    roomFloorComboBox->addItem("Floor 7");
    roomFloorComboBox->addItem("Floor 8");

    // Layout setup
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    // Hotel Name
    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotelNameLineEdit);
    mainLayout->addLayout(hotelNameLayout);

    // Room Floor
    QHBoxLayout *roomFloorLayout = new QHBoxLayout();
    roomFloorLayout->addWidget(new QLabel("Location:", this));
    roomFloorLayout->addWidget(roomFloorComboBox);
    mainLayout->addLayout(roomFloorLayout);

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
    buttonLayout->addWidget(createRoomButton);
    buttonLayout->addWidget(cancelButton);
    mainLayout->addLayout(buttonLayout);

    // Connect signals and slots
    connect(createRoomButton, &QPushButton::clicked, this, &CreateRoomDialog::onCreateRoomButtonClicked);
    connect(cancelButton, &QPushButton::clicked, this, &CreateRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Create Room");
}

CreateRoomDialog::~CreateRoomDialog()
{
    // Cleanup if necessary (currently handled by Qt's parent-child system)
}

void CreateRoomDialog::onCreateRoomButtonClicked()
{
    // Validate inputs
    bool valid = true;
    QString hotelName = hotelNameLineEdit->text();
    QString roomFloor = roomAvailableComboBox->currentText();
    QString roomNumber = roomNumberLineEdit->text();
    QString roomAvailable = roomAvailableComboBox->currentText();
    QString priceText = priceLineEdit->text();
    double price = priceText.toDouble();
    QString facilities = facilitiesLineEdit->text();

    if (hotelName.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Hotel name cannot be empty!");
        valid = false;
    }

    if (roomNumber.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Room number cannot be empty!");
        valid = false;
    }

    if (price <= 0) {
        QMessageBox::warning(this, "Input Error", "Price must be a positive number!");
        valid = false;
    }

    QStringList facilitiesList = facilities.split(",");

    Employee e = Employee(2, "employee1", "employee1@example.com", "password123");

    std::vector<std::string> room_facilities;
    for (const auto &facility : facilitiesList) {
        room_facilities.push_back(facility.toStdString());
    }

    bool is_available = roomAvailable == "Yes" ? 1 : 0;
    Room room = Room(99, roomFloor.toStdString(), roomNumber.toInt(), is_available , price , room_facilities);
    e.CreateRoom(hotelName.toStdString(), room);
    Room r = e.ReadRoom(hotelName.toStdString(), roomNumber.toInt());
    std::cout << "Room added with details: id = " << r.GetId() << " location = "
                << r.GetLocation() << " number = " << r.GetNumber() << " price = "
                << r.GetPrice() << " facilities = ";
    for (const auto &facility : r.GetFacilities())
    {
        std::cout << facility << " ";
    }
    std::cout << "\n";
    if (valid) {
        // Code to create the room can go here (e.g., calling a function to add the room to a database)
        QMessageBox::information(this, "Room Created", "The room has been created successfully!");
        accept();  // Close the dialog with success
    }
}