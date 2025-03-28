#include "include/DeleteRoomDialog.h"
#include <iostream>
#include <QMessageBox>
#include "../include/employee.h"
#include "../include/room.h"

DeleteRoomDialog::DeleteRoomDialog(QWidget *parent) : QDialog(parent)
{
    // Create the widgets
    hotelNameLineEdit = new QLineEdit(this);
    roomNumberLineEdit = new QLineEdit(this);

    deleteRoomButton = new QPushButton("Delete Room", this);
    cancelButton = new QPushButton("Cancel", this);
    
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
    
    // Buttons
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(deleteRoomButton);
    buttonLayout->addWidget(cancelButton);
    mainLayout->addLayout(buttonLayout);

    // Connect signals and slots
    connect(deleteRoomButton, &QPushButton::clicked, this, &DeleteRoomDialog::onDeleteRoomButtonClicked);
    connect(cancelButton, &QPushButton::clicked, this, &DeleteRoomDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Delete Room");
}

DeleteRoomDialog::~DeleteRoomDialog()
{
    // Cleanup if necessary (currently handled by Qt's parent-child system)
}

void DeleteRoomDialog::onDeleteRoomButtonClicked()
{
    bool valid = true;
    QString hotelName = hotelNameLineEdit->text();
    QString roomNumber = roomNumberLineEdit->text();

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