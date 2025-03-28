#include "include/LogInDialog.h"
#include "include/EmployeeGUI.h"
#include "include/CreateRoomDialog.h"
#include "include/ReadRoomDialog.h"
#include "include/UpdateRoomDialog.h"
#include "include/DeleteRoomDialog.h"
#include "ui/EmployeeUI/ui_EmployeeGUI.h"
#include "ui/EmployeeUI/ui_CreateRoomGUI.h"
#include "ui/EmployeeUI/ui_ReadRoomGUI.h"

#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QDebug>
#include <iostream>

#include "../include/client.h"
#include "../include/room.h"

EmployeeGUI::EmployeeGUI(QWidget *parent) 
    : QMainWindow(parent), ui(new Ui::EmployeeGUI)
{
    ui->setupUi(this);
    ui->createRoomButton->setVisible(false);
    ui->readRoomButton->setVisible(false);
    ui->updateRoomButton->setVisible(false);
    ui->deleteRoomButton->setVisible(false);
    ui->logOutButton->setVisible(false);
    connect(ui->logInButton, &QPushButton::clicked, this, &EmployeeGUI::openLogInDialog);
    connect(ui->createRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openCreateRoomDialog);
    connect(ui->readRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openReadRoomDialog);
    connect(ui->updateRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openUpdateRoomDialog);
    connect(ui->deleteRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openDeleteRoomDialog);
    connect(ui->logOutButton, &QPushButton::clicked, this, &EmployeeGUI::LogOutDialog);
}

EmployeeGUI::~EmployeeGUI()
{
    delete ui;
}

void EmployeeGUI::openLogInDialog()
{
    LogInDialog logInDialog(this, this);  
    if (logInDialog.exec() == QDialog::Accepted) 
    {
        ui->logInButton->setVisible(false);
        ui->createRoomButton->setVisible(true);
        ui->readRoomButton->setVisible(true);
        ui->updateRoomButton->setVisible(true);
        ui->deleteRoomButton->setVisible(true);
        ui->logOutButton->setVisible(true);
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
        std::cout << "Not logged in\n";
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
        std::cout << "Not logged in\n";
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
        std::cout << "Not logged in\n";
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
        std::cout << "Not logged in\n";
    }
}
void EmployeeGUI::LogOutDialog()
{
    employee_.Logout();
    ui->logInButton->setVisible(true);
    ui->createRoomButton->setVisible(false);
    ui->readRoomButton->setVisible(false);
    ui->updateRoomButton->setVisible(false);
    ui->deleteRoomButton->setVisible(false);
    ui->logOutButton->setVisible(false);
}