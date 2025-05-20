from Controllers.UserController import UserController
from Controllers.ClientController import ClientController
from PyQt5.QtWidgets import QApplication
import sys

def SwitchToUserView():
    win.hide()
    win2.showMaximized()

def SwitchToClientView():
    win.showMaximized()
    client_controller.ShowRooms()
    win2.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_controller = ClientController(SwitchToUserView)
    user_controller = UserController(SwitchToClientView)
    win = client_controller.GetGUI()
    win2 = user_controller.GetGUI()
    win.showMaximized()
    sys.exit(app.exec_())