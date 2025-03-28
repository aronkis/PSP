#ifndef UPDATE_ROOM_DIALOG_H
#define UPDATE_ROOM_DIALOG_H

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
    UpdateRoomDialog(QWidget *parent = nullptr);
    ~UpdateRoomDialog();

private slots:
    void OnUpdateRoomButtonClicked();

private:
    QLineEdit *hotel_name_line_edit_;
    QLineEdit *room_number_line_edit_;
    QComboBox *room_available_combo_box_;
    QLineEdit *price_line_edit_;
    QLineEdit *facilities_line_edit_;
    QPushButton *update_room_button_;
    QPushButton *cancel_button_;
};

#endif // UPDATEROOMDIALOG_H
