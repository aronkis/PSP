#ifndef CLIENT_GUI_H
#define CLIENT_GUI_H

#include <QLabel>
#include <QPushButton>
#include <QLineEdit>
#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class ClientGUI; }
QT_END_NAMESPACE

class ClientGUI : public QMainWindow
{
    Q_OBJECT

public:
    ClientGUI(QWidget *parent = nullptr);
    ~ClientGUI();

private slots:
    void OnSendButtonClicked();  

private:
    Ui::ClientGUI *ui_;
};

#endif
