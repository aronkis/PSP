#include "include/EmployeeGUI.h"
#include "ui/EmployeeUI/ui_EmployeeGUI.h"
#include "ui/EmployeeUI/ui_CreateRoomGUI.h"
#include "include/CreateRoomDialog.h"
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QDebug>
#include "../include/client.h"
#include "../include/room.h"
// #include "readroomdialog.h"
// #include "updateroomdialog.h"
// #include "deleteroomdialog.h"

EmployeeGUI::EmployeeGUI(QWidget *parent) 
    : QMainWindow(parent), ui(new Ui::EmployeeGUI)
{
    ui->setupUi(this);

    connect(ui->createRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openCreateRoomDialog);
    // connect(ui->readRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openReadRoomDialog);
    // connect(ui->updateRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openUpdateRoomDialog);
    // connect(ui->deleteRoomButton, &QPushButton::clicked, this, &EmployeeGUI::openDeleteRoomDialog);
}

EmployeeGUI::~EmployeeGUI()
{
    delete ui;
}

void EmployeeGUI::openCreateRoomDialog()
{
    CreateRoomDialog dialog(this);  
    if (dialog.exec() == QDialog::Accepted) {
    }
    else
    {
        dialog.close();
    }
}

// void MainWindow::openReadRoomDialog()
// {
//     ReadRoomDialog readDialog(this);
//     readDialog.exec();
// }

// void MainWindow::openUpdateRoomDialog()
// {
//     UpdateRoomDialog updateDialog(this);
//     updateDialog.exec();
// }

// void MainWindow::openDeleteRoomDialog()
// {
//     DeleteRoomDialog deleteDialog(this);
//     deleteDialog.exec();
// }
