#include <QMessageBox>

#include "include/DeleteRoomDialog.h"

#include "../include/employee.h"
#include "../include/room.h"

DeleteRoomDialog::DeleteRoomDialog(QWidget *parent) : QDialog(parent)
{
    hotel_name_line_edit_ = new QLineEdit(this);
    room_number_line_edit_ = new QLineEdit(this);

    delete_room_button_ = new QPushButton("Delete Room", this);
    cancel_button_ = new QPushButton("Cancel", this);
    
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    QHBoxLayout *hotelNameLayout = new QHBoxLayout();
    hotelNameLayout->addWidget(new QLabel("Hotel Name:", this));
    hotelNameLayout->addWidget(hotel_name_line_edit_);
    mainLayout->addLayout(hotelNameLayout);

    QHBoxLayout *roomNumberLayout = new QHBoxLayout();
    roomNumberLayout->addWidget(new QLabel("Room Number:", this));
    roomNumberLayout->addWidget(room_number_line_edit_);
    mainLayout->addLayout(roomNumberLayout);
    
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(delete_room_button_);
    buttonLayout->addWidget(cancel_button_);
    mainLayout->addLayout(buttonLayout);

    connect(delete_room_button_, &QPushButton::clicked, this, &DeleteRoomDialog::OnDeleteRoomButtonClicked);
    connect(cancel_button_, &QPushButton::clicked, this, &DeleteRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Delete Room");
}

DeleteRoomDialog::~DeleteRoomDialog()
{
}

void DeleteRoomDialog::OnDeleteRoomButtonClicked()
{
    bool valid = true;
    QString hotelName = hotel_name_line_edit_->text();
    QString roomNumber = room_number_line_edit_->text();

    if (hotelName.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Hotel name cannot be empty!");
        valid = false;
    }

    if (roomNumber.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Room number cannot be empty!");
        valid = false;
    }
    
    if (valid)
    {
        Employee e = Employee(2, "employee1", "employee1@example.com", "password123");
    
        try
        {
            e.DeleteRoom(hotelName.toStdString(), roomNumber.toInt());
            QMessageBox::information(this, "Room deleted", "The room has been deleted successfully!");
        }
        catch(const std::exception& e)
        {
            QMessageBox::information(this, "Invalid Input", e.what());
        }
    }
    
}