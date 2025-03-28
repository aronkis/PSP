#ifndef LOG_IN_DIALOG_H
#define LOG_IN_DIALOG_H

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
    void OnLogInButtonClicked();

private:
    QLineEdit *username_line_edit_;
    QLineEdit *password_line_edit_;
    QPushButton *log_in_button_;
    QPushButton *cancel_button_;
    EmployeeGUI *employeeGUI_;
};

#endif // DELETEROOMDIALOG_H
