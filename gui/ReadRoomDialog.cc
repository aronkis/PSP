#include <QMessageBox>

#include "include/ReadRoomDialog.h"

#include "../include/employee.h"
#include "../include/room.h"

ReadRoomDialog::ReadRoomDialog(QWidget *parent) 
    : QDialog(parent)
{
    hotel_name_line_edit_ = new QLineEdit(this);
    room_number_line_edit_ = new QLineEdit(this);

    read_room_button_ = new QPushButton("Read Room", this);
    cancel_button_ = new QPushButton("Cancel", this);

    room_id_label_ = new QLabel("Room ID: N/A", this);
    room_number_label_ = new QLabel("Number: N/A", this);
    room_location_label = new QLabel("Location: N/A", this);
    room_price_label = new QLabel("Price: N/A", this);
    room_availability_label_ = new QLabel("Available: N/A", this);
    room_facilities_label_ = new QLabel("Facilities: N/A", this);

    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotel_name_line_edit_);
    mainLayout->addLayout(hotelNameLayout);

    QHBoxLayout *roomNumberLayout = new QHBoxLayout();
    roomNumberLayout->addWidget(new QLabel("Room Number:", this));
    roomNumberLayout->addWidget(room_number_line_edit_);
    mainLayout->addLayout(roomNumberLayout);

    mainLayout->addWidget(room_id_label_);
    mainLayout->addWidget(room_number_label_);
    mainLayout->addWidget(room_location_label);
    mainLayout->addWidget(room_price_label);
    mainLayout->addWidget(room_availability_label_);
    mainLayout->addWidget(room_facilities_label_);

    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(read_room_button_);
    buttonLayout->addWidget(cancel_button_);
    mainLayout->addLayout(buttonLayout);

    connect(read_room_button_, &QPushButton::clicked, this, &ReadRoomDialog::OnReadRoomButtonClicked);
    connect(cancel_button_, &QPushButton::clicked, this, &QDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Read Room");
}

ReadRoomDialog::~ReadRoomDialog()
{
}

void ReadRoomDialog::OnReadRoomButtonClicked()
{
    QString hotelName = hotel_name_line_edit_->text();
    QString roomNumber = room_number_line_edit_->text();

    if (hotelName.isEmpty() || roomNumber.isEmpty()) 
    {
        QMessageBox::warning(this, "Input Error", "Please complete all input fields.");
        return;
    }

    Employee e = Employee(2, "employee1", "employee1@example.com", "password123");
    try
    {
        Room room = e.ReadRoom(hotelName.toStdString(), roomNumber.toInt());
        
        room_id_label_->setText("Room ID: " + QString::number(room.GetId()));
        room_number_label_->setText("Number: " + QString::number(room.GetNumber()));
        room_location_label->setText("Location: " + QString::fromStdString(room.GetLocation()));
        room_price_label->setText("Price: " + QString::number(room.GetPrice()));
        room_availability_label_->setText("Available: " + QString::fromStdString(room.GetAvailability() ? "Yes" : "No"));

        QStringList outputFacilities;
        for (const auto& facility : room.GetFacilities()) {
            outputFacilities << QString::fromStdString(facility);
        }
        room_facilities_label_->setText("Facilities: " + outputFacilities.join(" "));
    }
    catch(const std::exception& e)
    {
        room_id_label_->setText("Room ID: No rooms available");
        room_number_label_->setText("Number: N/A");
        room_location_label->setText("Location: N/A");
        room_price_label->setText("Price: N/A");
        room_availability_label_->setText("Available: N/A");
        room_facilities_label_->setText("Facilities: N/A");
        qDebug() << e.what();
    }
}

