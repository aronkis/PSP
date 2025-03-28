#ifndef READROOMDIALOG_H
#define READROOMDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QMainWindow>

class ReadRoomDialog : public QDialog
{
    Q_OBJECT

public:
    ReadRoomDialog(QWidget *parent = nullptr);
    ~ReadRoomDialog();

private slots:
    void onReadRoomClicked();

private:
    QLineEdit *hotelNameLineEdit;
    QLineEdit *roomNumberLineEdit;
    QPushButton *readRoomButton;
    QPushButton *cancelButton;

    QLabel *roomIdLabel;
    QLabel *roomNumberLabel;
    QLabel *roomLocationLabel;
    QLabel *roomPriceLabel;
    QLabel *roomAvailabilityLabel;
    QLabel *roomFacilitiesLabel;
};

#endif // READROOMDIALOG_H
