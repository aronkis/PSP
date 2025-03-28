#ifndef READROOMDIALOG_H
#define READROOMDIALOG_H

#include <QDialog>

namespace Ui {
class ReadRoomDialog;
}

class ReadRoomDialog : public QDialog
{
    Q_OBJECT

public:
    explicit ReadRoomDialog(QWidget *parent = nullptr);
    ~ReadRoomDialog();

private slots:
    void onReadRoomClicked();

private:
    Ui::ReadRoomDialog *ui;
};

#endif // READROOMDIALOG_H
