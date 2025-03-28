#ifndef DELETE_ROOM_DIALOG_H
#define DELETE_ROOM_DIALOG_H

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
    DeleteRoomDialog(QWidget *parent = nullptr);
    ~DeleteRoomDialog();

private slots:
    void OnDeleteRoomButtonClicked();

private:
    QLineEdit *hotel_name_line_edit_;
    QLineEdit *room_number_line_edit_;
    QPushButton *delete_room_button_;
    QPushButton *cancel_button_;
};

#endif // DELETEROOMDIALOG_H
