#include "../include/client.h"
#include "../include/room.h"
#include "../gui/include/ClientGUI.h"
#include <QApplication>
#include <iostream>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ClientGUI w;
    w.show();
    return a.exec();
}