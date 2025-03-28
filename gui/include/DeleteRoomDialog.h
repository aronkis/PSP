#ifndef DELETEROOMDIALOG_H
#define DELETEROOMDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QMainWindow>

class DeleteRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit DeleteRoomDialog(QWidget *parent = nullptr);
    ~DeleteRoomDialog();

private slots:
    void onDeleteRoomButtonClicked();

private:
    QLineEdit *hotelNameLineEdit;
    QLineEdit *roomNumberLineEdit;
    QPushButton *deleteRoomButton;
    QPushButton *cancelButton;
};

#endif // DELETEROOMDIALOG_H
