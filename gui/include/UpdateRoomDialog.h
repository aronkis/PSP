#ifndef UPDATEROOMDIALOG_H
#define UPDATEROOMDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QMainWindow>

class UpdateRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit UpdateRoomDialog(QWidget *parent = nullptr);
    ~UpdateRoomDialog();

private slots:
    void onUpdateRoomButtonClicked();

private:
    QLineEdit *hotelNameLineEdit;
    QLineEdit *roomNumberLineEdit;
    QComboBox *roomAvailableComboBox;
    QLineEdit *priceLineEdit;
    QLineEdit *facilitiesLineEdit;
    QPushButton *updateRoomButton;
    QPushButton *cancelButton;
};

#endif // UPDATEROOMDIALOG_H
