#ifndef READ_ROOM_DIALOG_H
#define READ_ROOM_DIALOG_H

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
    void OnReadRoomButtonClicked();

private:
    QLineEdit *hotel_name_line_edit_;
    QLineEdit *room_number_line_edit_;
    QPushButton *read_room_button_;
    QPushButton *cancel_button_;

    QLabel *room_id_label_;
    QLabel *room_number_label_;
    QLabel *room_location_label;
    QLabel *room_price_label;
    QLabel *room_availability_label_;
    QLabel *room_facilities_label_;
};

#endif // READROOMDIALOG_H
