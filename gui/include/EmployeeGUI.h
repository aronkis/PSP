#ifndef EMPLOYEE_GUI_H
#define EMPLOYEE_GUI_H

#include <QMainWindow>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include "CreateRoomDialog.h"
#include "../../include/employee.h"

QT_BEGIN_NAMESPACE
namespace Ui {class EmployeeGUI;}
QT_END_NAMESPACE

class EmployeeGUI : public QMainWindow
{
    Q_OBJECT

public:
    EmployeeGUI(QWidget *parent = nullptr);
    ~EmployeeGUI();
    void setEmployee(Employee employee) { employee_ = employee; }

private slots:
    void openLogInDialog();
    void openCreateRoomDialog();
    void openReadRoomDialog();
    void openUpdateRoomDialog();
    void openDeleteRoomDialog();
    void LogOutDialog();

private:
    Ui::EmployeeGUI *ui_;
    Employee employee_;
};
#endif
