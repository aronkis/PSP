#ifndef EMPLOYEE_GUI_H
#define EMPLOYEE_GUI_H

#include <QMainWindow>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include "CreateRoomDialog.h"
// #include "readroomdialog.h"
// #include "updateroomdialog.h"
// #include "deleteroomdialog.h"

QT_BEGIN_NAMESPACE
namespace Ui {class EmployeeGUI;}
QT_END_NAMESPACE

class EmployeeGUI : public QMainWindow
{
    Q_OBJECT

public:
    EmployeeGUI(QWidget *parent = nullptr);
    ~EmployeeGUI();

private slots:
    void openCreateRoomDialog();
    // void openReadRoomDialog();
    // void openUpdateRoomDialog();
    // void openDeleteRoomDialog();

private:
    Ui::EmployeeGUI *ui;
};
#endif
