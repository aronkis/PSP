#ifndef LOGINDIALOG_H
#define LOGINDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QMainWindow>
#include "EmployeeGUI.h"


class LogInDialog : public QDialog
{
    Q_OBJECT

public:
    LogInDialog(EmployeeGUI *employeeGUI, QWidget *parent = nullptr);
    ~LogInDialog();

private slots:
    void onLogInButtonClicked();

private:
    QLineEdit *usernameLineEdit;
    QLineEdit *passwordLineEdit;
    QPushButton *logInButton;
    QPushButton *cancelButton;
    EmployeeGUI *employeeGUI;
};

#endif // DELETEROOMDIALOG_H
