
#include <QMessageBox>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QDebug>

#include "include/LogInDialog.h"
#include "include/EmployeeGUI.h"
#include "include/CreateRoomDialog.h"
#include "include/ReadRoomDialog.h"
#include "include/UpdateRoomDialog.h"
#include "include/DeleteRoomDialog.h"
#include "ui/EmployeeUI/ui_EmployeeGUI.h"
#include "ui/EmployeeUI/ui_CreateRoomGUI.h"
#include "ui/EmployeeUI/ui_ReadRoomGUI.h"

#include "../include/client.h"
#include "../include/room.h"

EmployeeGUI::EmployeeGUI(QWidget *parent) 
    : QMainWindow(parent), ui_(new Ui::EmployeeGUI)
{
    ui_->setupUi(this);
    ui_->create_room_button_->setVisible(false);
    ui_->read_room_button_->setVisible(false);
    ui_->update_room_button_->setVisible(false);
    ui_->delete_room_button_->setVisible(false);
    ui_->logOutButton->setVisible(false);
    connect(ui_->log_in_button_, &QPushButton::clicked, this, &EmployeeGUI::openLogInDialog);
    connect(ui_->create_room_button_, &QPushButton::clicked, this, &EmployeeGUI::openCreateRoomDialog);
    connect(ui_->read_room_button_, &QPushButton::clicked, this, &EmployeeGUI::openReadRoomDialog);
    connect(ui_->update_room_button_, &QPushButton::clicked, this, &EmployeeGUI::openUpdateRoomDialog);
    connect(ui_->delete_room_button_, &QPushButton::clicked, this, &EmployeeGUI::openDeleteRoomDialog);
    connect(ui_->logOutButton, &QPushButton::clicked, this, &EmployeeGUI::LogOutDialog);
}

EmployeeGUI::~EmployeeGUI()
{
    delete ui_;
}

void EmployeeGUI::openLogInDialog()
{
    LogInDialog logInDialog(this, this);  
    if (logInDialog.exec() == QDialog::Accepted) 
    {
        ui_->log_in_button_->setVisible(false);
        ui_->create_room_button_->setVisible(true);
        ui_->read_room_button_->setVisible(true);
        ui_->update_room_button_->setVisible(true);
        ui_->delete_room_button_->setVisible(true);
        ui_->logOutButton->setVisible(true);
    }
    else
    {
        logInDialog.close();
    }
}

void EmployeeGUI::openCreateRoomDialog()
{
    if (employee_.GetLoggedIn())
    {
        CreateRoomDialog createDialog(this);  
        if (createDialog.exec() == QDialog::Accepted) 
        {
        }
        else
        {
            createDialog.close();
        }
    }
    else
    {
        QMessageBox::information(this, "Not permitted.", "The user is not authenticated!");
    }
}

void EmployeeGUI::openReadRoomDialog()
{
    if (employee_.GetLoggedIn())
    {
        ReadRoomDialog readDialog(this);
        if (readDialog.exec() == QDialog::Accepted) 
        {
        }
        else
        {
            readDialog.close();
        }
    }
    else
    {
        QMessageBox::information(this, "Not permitted.", "The user is not authenticated!");
    }
}

void EmployeeGUI::openUpdateRoomDialog()
{
    if (employee_.GetLoggedIn())
    {
        UpdateRoomDialog updateDialog(this);
        if (updateDialog.exec() == QDialog::Accepted) 
        {
        }
        else
        {
            updateDialog.close();
        }    
    }
    else
    {
        QMessageBox::information(this, "Not permitted.", "The user is not authenticated!");
    }
}

void EmployeeGUI::openDeleteRoomDialog()
{
    if (employee_.GetLoggedIn())
    {
        DeleteRoomDialog deleteDialog(this);
        if (deleteDialog.exec() == QDialog::Accepted) 
        {
        }
        else
        {
            deleteDialog.close();
        }  
    }
    else
    {
        QMessageBox::information(this, "Not permitted.", "The user is not authenticated!");
    }
}
void EmployeeGUI::LogOutDialog()
{
    employee_.Logout();
    ui_->log_in_button_->setVisible(true);
    ui_->create_room_button_->setVisible(false);
    ui_->read_room_button_->setVisible(false);
    ui_->update_room_button_->setVisible(false);
    ui_->delete_room_button_->setVisible(false);
    ui_->logOutButton->setVisible(false);
}