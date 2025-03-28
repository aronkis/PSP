#include "../gui/include/EmployeeGUI.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    EmployeeGUI w;
    w.show();
    return a.exec();
}