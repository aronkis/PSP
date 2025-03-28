#ifndef CREATE_ROOM_DIALOG_H
#define CREATE_ROOM_DIALOG_H

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
    CreateRoomDialog(QWidget *parent = nullptr);
    ~CreateRoomDialog();

private slots:
    void OnCreateRoomButtonClicked();

private:
    QLineEdit *hotel_name_line_edit_;
    QLineEdit *room_number_line_edit_;
    QComboBox *room_available_combo_box_;
    QComboBox *room_floor_combo_box_;
    QLineEdit *price_line_edit_;
    QLineEdit *facilities_line_edit_;
    QPushButton *create_room_button_;
    QPushButton *cancel_button_;
};

#endif
