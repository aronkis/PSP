#include "include/LogInDialog.h"
#include <iostream>
#include <QMessageBox>
#include "../include/employee.h"

LogInDialog::LogInDialog(EmployeeGUI *employeeGUI, QWidget *parent)
    : QDialog(parent), employeeGUI(employeeGUI)
{
    // Create the widgets
    usernameLineEdit = new QLineEdit(this);
    passwordLineEdit = new QLineEdit(this);

    logInButton = new QPushButton("Log In", this);
    cancelButton = new QPushButton("Cancel", this);
    
    // Layout setup
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    // Username
    QHBoxLayout *usernameLayout = new QHBoxLayout();
    usernameLayout->addWidget(new QLabel("Username:", this));
    usernameLayout->addWidget(usernameLineEdit);
    mainLayout->addLayout(usernameLayout);

    // Password
    QHBoxLayout *passwordLayout = new QHBoxLayout();
    passwordLayout->addWidget(new QLabel("Password:", this));
    passwordLineEdit->setEchoMode(QLineEdit::Password);
    passwordLayout->addWidget(passwordLineEdit);
    mainLayout->addLayout(passwordLayout);
    
    // Buttons
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(logInButton);
    buttonLayout->addWidget(cancelButton);
    mainLayout->addLayout(buttonLayout);

    // Connect signals and slots
    connect(logInButton, &QPushButton::clicked, this, &LogInDialog::onLogInButtonClicked);
    connect(cancelButton, &QPushButton::clicked, this, &LogInDialog::reject);

    setLayout(mainLayout);
    setWindowTitle("Log In");
}

LogInDialog::~LogInDialog()
{
    // Cleanup if necessary (currently handled by Qt's parent-child system)
}

void LogInDialog::onLogInButtonClicked()
{
    bool valid = true;
    QString username = usernameLineEdit->text();
    QString password = passwordLineEdit->text();

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
                employeeGUI->setEmployee(employee);
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