#ifndef UPDATEROOMDIALOG_H
#define UPDATEROOMDIALOG_H

#include <QDialog>

namespace Ui {
class UpdateRoomDialog;
}

class UpdateRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit UpdateRoomDialog(QWidget *parent = nullptr);
    ~UpdateRoomDialog();

private slots:
    void onUpdateRoomClicked();

private:
    Ui::UpdateRoomDialog *ui;
};

#endif // UPDATEROOMDIALOG_H
