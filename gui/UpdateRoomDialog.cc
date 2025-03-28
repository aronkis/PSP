#include <QMessageBox>

#include "include/UpdateRoomDialog.h"

#include "../include/employee.h"
#include "../include/room.h"

UpdateRoomDialog::UpdateRoomDialog(QWidget *parent) : QDialog(parent)
{
    hotel_name_line_edit_ = new QLineEdit(this);
    room_number_line_edit_ = new QLineEdit(this);
    price_line_edit_ = new QLineEdit(this);
    room_available_combo_box_ = new QComboBox(this);
    facilities_line_edit_ = new QLineEdit(this);
    update_room_button_ = new QPushButton("Update Room", this);
    cancel_button_ = new QPushButton("Cancel", this);

    room_available_combo_box_->addItem("Yes");
    room_available_combo_box_->addItem("No");

    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotel_name_line_edit_);
    mainLayout->addLayout(hotelNameLayout);

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
    buttonLayout->addWidget(update_room_button_);
    buttonLayout->addWidget(cancel_button_);
    mainLayout->addLayout(buttonLayout);

    connect(update_room_button_, &QPushButton::clicked, this, &UpdateRoomDialog::OnUpdateRoomButtonClicked);
    connect(cancel_button_, &QPushButton::clicked, this, &UpdateRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Update Room");
}

UpdateRoomDialog::~UpdateRoomDialog()
{
}

void UpdateRoomDialog::OnUpdateRoomButtonClicked()
{
    bool valid = true;
    QString hotelName = hotel_name_line_edit_->text();
    QString roomNumber = room_number_line_edit_->text();
    QString roomAvailable = room_available_combo_box_->currentText();
    QString priceText = price_line_edit_->text();
    double price;
    QString facilities = facilities_line_edit_->text();

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