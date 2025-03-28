#include <QMessageBox>

#include "include/CreateRoomDialog.h"

#include "../include/employee.h"
#include "../include/room.h"

CreateRoomDialog::CreateRoomDialog(QWidget *parent) : QDialog(parent)
{
    hotel_name_line_edit_ = new QLineEdit(this);
    room_floor_combo_box_ = new QComboBox(this);
    room_number_line_edit_ = new QLineEdit(this);
    price_line_edit_ = new QLineEdit(this);
    room_available_combo_box_ = new QComboBox(this);
    facilities_line_edit_ = new QLineEdit(this);
    create_room_button_ = new QPushButton("Create Room", this);
    cancel_button_ = new QPushButton("Cancel", this);

    room_available_combo_box_->addItem("Yes");
    room_available_combo_box_->addItem("No");

    room_floor_combo_box_->addItem("Floor 1");
    room_floor_combo_box_->addItem("Floor 2");
    room_floor_combo_box_->addItem("Floor 3");
    room_floor_combo_box_->addItem("Floor 4");
    room_floor_combo_box_->addItem("Floor 5");
    room_floor_combo_box_->addItem("Floor 6");
    room_floor_combo_box_->addItem("Floor 7");
    room_floor_combo_box_->addItem("Floor 8");

    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotel_name_line_edit_);
    mainLayout->addLayout(hotelNameLayout);

    QHBoxLayout *roomFloorLayout = new QHBoxLayout();
    roomFloorLayout->addWidget(new QLabel("Location:", this));
    roomFloorLayout->addWidget(room_floor_combo_box_);
    mainLayout->addLayout(roomFloorLayout);

    QHBoxLayout *roomNumberLayout = new QHBoxLayout();
    roomNumberLayout->addWidget(new QLabel("Room Number:", this));
    roomNumberLayout->addWidget(room_number_line_edit_);
    mainLayout->addLayout(roomNumberLayout);

    QHBoxLayout *priceLayout = new QHBoxLayout();
    priceLayout->addWidget(new QLabel("Price:", this));
    priceLayout->addWidget(price_line_edit_);
    mainLayout->addLayout(priceLayout);

    QHBoxLayout *roomTypeLayout = new QHBoxLayout();
    roomTypeLayout->addWidget(new QLabel("Available:", this));
    roomTypeLayout->addWidget(room_available_combo_box_);
    mainLayout->addLayout(roomTypeLayout);

    QHBoxLayout *facilitiesLayout = new QHBoxLayout();
    facilitiesLayout->addWidget(new QLabel("Facilities:", this));
    facilitiesLayout->addWidget(facilities_line_edit_);
    mainLayout->addLayout(facilitiesLayout);

    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(create_room_button_);
    buttonLayout->addWidget(cancel_button_);
    mainLayout->addLayout(buttonLayout);

    connect(create_room_button_, &QPushButton::clicked, this, &CreateRoomDialog::OnCreateRoomButtonClicked);
    connect(cancel_button_, &QPushButton::clicked, this, &CreateRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Create Room");
}

CreateRoomDialog::~CreateRoomDialog()
{
}

void CreateRoomDialog::OnCreateRoomButtonClicked()
{
    bool valid = true;
    QString hotelName = hotel_name_line_edit_->text();
    QString roomFloor = room_available_combo_box_->currentText();
    QString roomNumber = room_number_line_edit_->text();
    QString roomAvailable = room_available_combo_box_->currentText();
    QString priceText = price_line_edit_->text();
    double price = priceText.toDouble();
    QString facilities = facilities_line_edit_->text();

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
    
    if (valid) {
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

        QMessageBox::information(this, "Room Created", "The room has been created successfully!");
        accept();
    }
}