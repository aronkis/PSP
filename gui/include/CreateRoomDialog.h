#ifndef CREATEROOMDIALOG_H
#define CREATEROOMDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QMainWindow>

class CreateRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit CreateRoomDialog(QWidget *parent = nullptr);
    ~CreateRoomDialog();

private slots:
    void onCreateRoomButtonClicked();

private:
    QLineEdit *hotelNameLineEdit;
    QLineEdit *roomNumberLineEdit;
    QComboBox *roomAvailableComboBox;
    QComboBox *roomFloorComboBox;
    QLineEdit *priceLineEdit;
    QLineEdit *facilitiesLineEdit;
    QPushButton *createRoomButton;
    QPushButton *cancelButton;
};

#endif
