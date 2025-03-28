#include <QMessageBox>

#include "include/LogInDialog.h"

#include "../include/employee.h"

LogInDialog::LogInDialog(EmployeeGUI *employeeGUI, QWidget *parent)
    : QDialog(parent), employeeGUI_(employeeGUI)
{
    username_line_edit_ = new QLineEdit(this);
    password_line_edit_ = new QLineEdit(this);

    log_in_button_ = new QPushButton("Log In", this);
    cancel_button_ = new QPushButton("Cancel", this);
    
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    QHBoxLayout *usernameLayout = new QHBoxLayout();
    usernameLayout->addWidget(new QLabel("Username:", this));
    usernameLayout->addWidget(username_line_edit_);
    mainLayout->addLayout(usernameLayout);

    QHBoxLayout *passwordLayout = new QHBoxLayout();
    passwordLayout->addWidget(new QLabel("Password:", this));
    password_line_edit_->setEchoMode(QLineEdit::Password);
    passwordLayout->addWidget(password_line_edit_);
    mainLayout->addLayout(passwordLayout);
    
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(log_in_button_);
    buttonLayout->addWidget(cancel_button_);
    mainLayout->addLayout(buttonLayout);

    connect(log_in_button_, &QPushButton::clicked, this, &LogInDialog::OnLogInButtonClicked);
    connect(cancel_button_, &QPushButton::clicked, this, &LogInDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Log In");
}

LogInDialog::~LogInDialog()
{
}

void LogInDialog::OnLogInButtonClicked()
{
    bool valid = true;
    QString username = username_line_edit_->text();
    QString password = password_line_edit_->text();

    if (username.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Username required ");
        valid = false;
    }

    if (password.isEmpty()) {
        QMessageBox::warning(this, "Input Error", "Password required ");
        valid = false;
    }
    
    if (valid)
    {
        try
        {
            Employee employee = Employee(username.toStdString(), password.toStdString());
            employee.Login();
            if (employee.GetLoggedIn())
            {
                employeeGUI_->setEmployee(employee);
                QMessageBox::information(this, "Logged in", "Logged in successfully!");
                accept();
            }
            else
            {
                QMessageBox::information(this, "Wrong username or password", "Please check your username and password.");
            }
        }
        catch(const std::exception& e)
        {
            QMessageBox::information(this, "Wrong username or password", e.what());
        }
        
        
    }
    
}