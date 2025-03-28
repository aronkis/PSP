#ifndef DELETEROOMDIALOG_H
#define DELETEROOMDIALOG_H

#include <QDialog>

namespace Ui {
class DeleteRoomDialog;
}

class DeleteRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit DeleteRoomDialog(QWidget *parent = nullptr);
    ~DeleteRoomDialog();

private slots:
    void onDeleteRoomClicked();

private:
    Ui::DeleteRoomDialog *ui;
};

#endif // DELETEROOMDIALOG_H
