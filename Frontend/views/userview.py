from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTableWidget, QTableWidgetItem, QComboBox,
    QMessageBox, QTabWidget, QHeaderView, QDateEdit, QLabel
)
from PyQt5.QtCore import Qt, QDate

class UserView(QWidget):
    def __init__(self):
        super().__init__()
        self.__user_authenticated = False
        self.setWindowTitle("Hotel Room Management")
        self.Init_ui()

    def Init_ui(self) -> None:
        self.__layout = QVBoxLayout()
        self.__main_tab_widget = QTabWidget()

        self.__language_dropdown = QComboBox()
        self.__language_dropdown.addItems(["EN", "RO", "DE"])
        self.__language_dropdown.setFixedWidth(60)
        self.__language_dropdown.currentIndexChanged.connect(self.TranslateUI)

        self.__user_tab_message_1 = QLabel("You do not have permission to manage users.")
        self.__user_tab_message_1.setStyleSheet("color: red; font-weight: bold;")
        self.__user_tab_message_1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.__user_tab_message_2 = QLabel("You do not have permission to manage users.")
        self.__user_tab_message_2.setStyleSheet("color: red; font-weight: bold;")
        self.__user_tab_message_2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.__user_tab_message_3 = QLabel("You do not have permission to manage users.")
        self.__user_tab_message_3.setStyleSheet("color: red; font-weight: bold;")
        self.__user_tab_message_3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.__user_tab_message_4 = QLabel("You do not have permission to manage users.")
        self.__user_tab_message_4.setStyleSheet("color: red; font-weight: bold;")
        self.__user_tab_message_4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        main_tab_layout = QVBoxLayout()

        lang_logout_layout = QHBoxLayout()
        self.__logout = QPushButton("Logout")
        self.__logout.setFixedWidth(100)
        lang_logout_layout.addWidget(self.__language_dropdown)
        lang_logout_layout.addWidget(self.__logout)
        lang_logout_layout.setAlignment(Qt.AlignLeft)
        self.__logout.hide()
        main_tab_layout.addLayout(lang_logout_layout)

        self.__login_widget = QWidget()
        __login_layout = QHBoxLayout()
        self.__username_input = QLineEdit()
        self.__username_input.setPlaceholderText("Username")
        self.__password_input = QLineEdit()
        self.__password_input.setPlaceholderText("Password")
        self.__password_input.setEchoMode(QLineEdit.Password)
        self.__login_button = QPushButton("Login")
        __login_layout.addWidget(self.__username_input)
        __login_layout.addWidget(self.__password_input)
        __login_layout.addWidget(self.__login_button)
        self.__login_widget.setLayout(__login_layout)
        main_tab_layout.addWidget(self.__login_widget)

        self.__employee_tab_widget = QTabWidget()  
        self.__employee_tab_widget.hide()  

        sub_tab_1 = QWidget()
        sub_tab_1_layout = QVBoxLayout()
        sub_tab_1_layout.addWidget(self.__user_tab_message_1)
        self.__user_tab_message_1.setAlignment(Qt.AlignHCenter)

        self.__table = QTableWidget()
        self.__table.setColumnCount(7)
        self.__table.setHorizontalHeaderLabels(["ID", "Hotel Name", "Number", "Location", "Price", "Position", "Facilities"])
        self.__table.hide()
        self.__table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        sub_tab_1_layout.addWidget(self.__table)

        self.__controls_widget = QWidget()
        __controls_layout = QVBoxLayout()

        __filter_layout = QHBoxLayout()
        self.__loc_input = QLineEdit()
        self.__loc_input.setPlaceholderText("Location")
        self.__price_input = QLineEdit()
        self.__price_input.setPlaceholderText("Max Price")
        self.__pos_input = QLineEdit()
        self.__pos_input.setPlaceholderText("Position")
        self.__fac_input = QLineEdit()
        self.__fac_input.setPlaceholderText("Facility")
        self.__filter_button = QPushButton("Show Rooms")
        __filter_layout.addWidget(self.__loc_input)
        __filter_layout.addWidget(self.__price_input)
        __filter_layout.addWidget(self.__pos_input)
        __filter_layout.addWidget(self.__fac_input)
        __filter_layout.addWidget(self.__filter_button)

        __room_crud_layout = QHBoxLayout()
        self.__add_button = QPushButton("Add Room")
        self.__update_button = QPushButton("Update Room")
        self.__delete_button = QPushButton("Delete Room")
        __room_crud_layout.addWidget(self.__add_button)
        __room_crud_layout.addWidget(self.__update_button)
        __room_crud_layout.addWidget(self.__delete_button)
        __reservation_layout = QHBoxLayout()
        self.__start_date_edit = QDateEdit()
        self.__start_date_edit.setCalendarPopup(True)
        self.__start_date_edit.setDate(QDate.currentDate())
        self.__start_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.__end_date_edit = QDateEdit()
        self.__end_date_edit.setCalendarPopup(True)
        self.__end_date_edit.setDate(QDate.currentDate())
        self.__end_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.__client_id_input = QLineEdit()
        self.__client_id_input.setPlaceholderText("Client ID")
        self.__client_id_input.setFixedWidth(500)
        self.__reserve_room_button = QPushButton("Reserve Room")
        __reservation_layout.addWidget(self.__client_id_input)
        __reservation_layout.addWidget(self.__start_date_edit)
        __reservation_layout.addWidget(self.__end_date_edit)
        __reservation_layout.addWidget(self.__reserve_room_button)

        __controls_layout.addLayout(__filter_layout)
        __controls_layout.addLayout(__room_crud_layout)
        self.__controls_widget.setLayout(__controls_layout)
        self.__controls_widget.hide()

        sub_tab_1_layout.addWidget(self.__controls_widget)
        sub_tab_1_layout.addLayout(__reservation_layout)  
        sub_tab_1.setLayout(sub_tab_1_layout)

        sub_tab_2 = QWidget()
        sub_tab_2_layout = QVBoxLayout()
        sub_tab_2_layout.addWidget(self.__user_tab_message_2)
        self.__user_tab_message_2.setAlignment(Qt.AlignHCenter)

        self.__client_table = QTableWidget()
        self.__client_table.setColumnCount(4)
        self.__client_table.setHorizontalHeaderLabels(["Client Id", "Client Name", "Client Email", "Client Phone Number"])
        sub_tab_2_layout.addWidget(self.__client_table)

        __client_crud_layout = QHBoxLayout()
        self.__add_client_button = QPushButton("Add Client")
        self.__update_client_button = QPushButton("Update Client")
        self.__delete_client_button = QPushButton("Delete Client")
        __client_crud_layout.addWidget(self.__add_client_button)
        __client_crud_layout.addWidget(self.__update_client_button)
        __client_crud_layout.addWidget(self.__delete_client_button)
        self.__client_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        sub_tab_2_layout.addLayout(__client_crud_layout)
        sub_tab_2.setLayout(sub_tab_2_layout)

        sub_tab_3 = QWidget()
        sub_tab_3_layout = QHBoxLayout()

        stats_button_vlayout = QVBoxLayout()
        self.__show_floors_button = QPushButton("Show Floors")
        self.__show_cities_button = QPushButton("Show Cities")
        self.__save_data_button = QPushButton("Save data")
        self.__save_format_dropdown = QComboBox()
        self.__save_format_dropdown.addItems(["csv", "json", "xml", "txt"])

        stats_button_vlayout.addWidget(self.__user_tab_message_3)
        self.__user_tab_message_3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        stats_button_vlayout.addWidget(self.__show_floors_button)
        stats_button_vlayout.addWidget(self.__show_cities_button)
        stats_button_vlayout.addWidget(self.__save_data_button)
        stats_button_vlayout.addWidget(self.__save_format_dropdown)
        stats_button_vlayout.addStretch(1)

        self.__graphics_zone = QWidget()
        self.__graphics_zone.setMinimumSize(300, 300)

        sub_tab_3_layout.addLayout(stats_button_vlayout, 1) 
        sub_tab_3_layout.addWidget(self.__graphics_zone, 3)  

        sub_tab_3.setLayout(sub_tab_3_layout)

        sub_tab_4 = QWidget()
        sub_tab_4_layout = QVBoxLayout()


        self.__user_table = QTableWidget()
        self.__user_table.setColumnCount(4)
        self.__user_table.setHorizontalHeaderLabels(["User ID", "User Name", "User Password", "User Role"])
        self.__user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        self.__add_user_button = QPushButton("Add User")
        self.__update_user_button = QPushButton("Update User")
        self.__remove_user_button = QPushButton("Delete User")
        self.__list_user_button = QPushButton("List User")

        self.__user_role_dropdown = QComboBox()
        self.__user_role_dropdown.addItems(["", "Admin", "Employee"])

        __user_crud_layout = QHBoxLayout()
        __user_crud_layout.addWidget(self.__add_user_button)
        __user_crud_layout.addWidget(self.__update_user_button)
        __user_crud_layout.addWidget(self.__remove_user_button)

        __role_list_layout = QHBoxLayout()
        __role_list_layout.addWidget(self.__user_role_dropdown)
        __role_list_layout.addWidget(self.__list_user_button)

        sub_tab_4_layout.addWidget(self.__user_tab_message_4)
        self.__user_tab_message_4.setAlignment(Qt.AlignHCenter)
        sub_tab_4_layout.addWidget(self.__user_table, stretch=1)
        sub_tab_4_layout.addLayout(__user_crud_layout)
        sub_tab_4_layout.addLayout(__role_list_layout)

        self.__user_tab_message_4.hide()  
        sub_tab_4.setLayout(sub_tab_4_layout)

        self.__employee_tab_widget.addTab(sub_tab_1, "Room Management")
        self.__employee_tab_widget.addTab(sub_tab_2, "Client Management")
        self.__employee_tab_widget.addTab(sub_tab_3, "Statistics")
        self.__employee_tab_widget.addTab(sub_tab_4, "User Management")

        main_tab_layout.addWidget(self.__employee_tab_widget)

        self.__layout.addLayout(main_tab_layout)
        self.setLayout(self.__layout)

    def Update(self, rooms: list[list[str]]) -> None:
        self.__table.setRowCount(len(rooms))  
        for row_idx, room in enumerate(rooms):
            for col_idx, value in enumerate(room):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.__table.setItem(row_idx, col_idx, item)
    
    def UpdateClients(self, clients: list[list[str]]) -> None:
        self.__client_table.setRowCount(len(clients))  
        for row_idx, client in enumerate(clients):
            for col_idx, value in enumerate(client):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter) 
                self.__client_table.setItem(row_idx, col_idx, item)

    def UpdateUsers(self, users: list[list[str]]) -> None:
        self.__user_table.setRowCount(len(users))  
        for row_idx, user in enumerate(users):
            for col_idx, value in enumerate(user):
                if (col_idx == 3):
                    value = "Admin" if value == 1 else "Employee"
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  
                self.__user_table.setItem(row_idx, col_idx, item)

    def ShowAdminTabMessage(self, show: bool):
        if show:
            self.__add_user_button.hide()
            self.__update_user_button.hide()
            self.__remove_user_button.hide()
            self.__list_user_button.hide()
            self.__user_role_dropdown.hide()
            self.__user_table.hide()
            self.__user_tab_message_4.show()
        else:
            self.__add_user_button.show()
            self.__update_user_button.show()
            self.__remove_user_button.show()
            self.__list_user_button.show()
            self.__user_role_dropdown.show()
            self.__user_table.show()
            self.__user_tab_message_4.hide()

    def ShowUserTabMessage(self, show: bool):
        if show:
            self.__table.hide()
            self.__controls_widget.hide()
            self.__reserve_room_button.hide()
            self.__client_id_input.hide()
            self.__start_date_edit.hide()
            self.__end_date_edit.hide()
            self.__client_table.hide()
            self.__add_client_button.hide()
            self.__update_client_button.hide()
            self.__delete_client_button.hide()
            self.__show_floors_button.hide()
            self.__show_cities_button.hide()
            self.__save_data_button.hide()
            self.__save_format_dropdown.hide()
            self.__graphics_zone.hide()
            self.__user_tab_message_1.show()
            self.__user_tab_message_2.show()
            self.__user_tab_message_3.show()
        else:
            self.__table.show()
            self.__controls_widget.show()
            self.__reserve_room_button.show()
            self.__logout.show()
            self.__client_id_input.show()
            self.__start_date_edit.show()
            self.__end_date_edit.show()
            self.__client_table.show()
            self.__add_client_button.show()
            self.__update_client_button.show()
            self.__delete_client_button.show()
            self.__show_floors_button.show()
            self.__show_cities_button.show()
            self.__save_data_button.show()
            self.__save_format_dropdown.show()
            self.__graphics_zone.show()
            self.__user_tab_message_4.show()
            self.__user_tab_message_1.hide()
            self.__user_tab_message_2.hide()
            self.__user_tab_message_3.hide()

    def GetDropdownValue(self) -> str:
        return self.__save_format_dropdown.currentText()
    
    def GetUserRoleDropdownValue(self) -> str:
        return self.__user_role_dropdown.currentText()
    
    def GetGraphicZone(self):
        return self.__graphics_zone
    
    def SetGraphicZone(self, canvas) -> None:
        self.__graphics_zone.layout().addWidget(canvas)
   
    def HideMainTab(self):
        self.__main_tab_widget.tabBar().hide()

    def SetUserAuthenticated(self) -> None:
        self.__user_authenticated = True
        self.__login_widget.hide() 
        self.__employee_tab_widget.show()  
        self.__logout.show()
    
    def SetUserUnauthenticated(self) -> None:
        self.__user_authenticated = False
        self.__login_widget.show() 
        self.__employee_tab_widget.hide()  
        self.__logout.hide()
    
    def SetFocusOnUsername(self) -> None:
        self.__username_input.setFocus()

    def GetUsernameInput(self) -> str:
        return self.__username_input.text()

    def SetUsernameInput(self, username: str) -> None:
        self.__username_input.setText(username)

    def GetPasswordInput(self) -> str:
        return self.__password_input.text()

    def SetPasswordInput(self, password: str) -> None:
        self.__password_input.setText(password)

    def GetLocationInput(self) -> str:
        return self.__loc_input.text()

    def GetPriceInput(self) -> str:
        return self.__price_input.text()

    def GetPositionInput(self) -> str:
        return self.__pos_input.text()

    def GetFacilitiesInput(self) -> str:
        return self.__fac_input.text()

    def SetLoginFunction(self, callback: callable = None) -> None:
        self.__login_button.clicked.connect(callback)

    def SetFilterFunction(self, callback: callable) -> None:
        self.__filter_button.clicked.connect(callback)

    def SetAddFunction(self, callback: callable) -> None:
        self.__add_button.clicked.connect(callback)

    def SetUpdateFunction(self, callback: callable) -> None:
        self.__update_button.clicked.connect(callback)

    def SetDeleteFunction(self, callback: callable) -> None:
        self.__delete_button.clicked.connect(callback)

    def SetAddClientFunction(self, callback: callable) -> None:
        self.__add_client_button.clicked.connect(callback)
    
    def SetUpdateClientFunction(self, callback: callable) -> None:
        self.__update_client_button.clicked.connect(callback)
    
    def SetDeleteClientFunction(self, callback: callable) -> None:
        self.__delete_client_button.clicked.connect(callback)

    def SetRoomFloorsFunction(self, callback: callable) -> None:
        self.__show_floors_button.clicked.connect(callback)
    
    def SetRoomCitiesFunction(self, callback: callable) -> None:
        self.__show_cities_button.clicked.connect(callback)

    def SetSaveDataFunction(self, callback: callable) -> None:
        self.__save_data_button.clicked.connect(callback)

    def SetTabChangedFunction(self, callback: callable) -> None:
        self.__employee_tab_widget.currentChanged.connect(callback)

    def SetAddUserFunction(self, callback: callable) -> None:
        self.__add_user_button.clicked.connect(callback)
    
    def SetUpdateUserFunction(self, callback: callable) -> None:
        self.__update_user_button.clicked.connect(callback)
    
    def SetDeleteUserFunction(self, callback: callable) -> None:
        self.__remove_user_button.clicked.connect(callback)
    
    def SetListUserFunction(self, callback: callable) -> None:
        self.__list_user_button.clicked.connect(callback)
    
    def SetReserveRoomButtonFunction(self, callback: callable) -> None:
        self.__reserve_room_button.clicked.connect(callback)
    
    def SetLogoutButtonFunction(self, callback: callable) -> None:
        self.__logout.clicked.connect(callback)

    def GetCurrentRow(self) -> int:
        return self.__table.currentRow()

    def GetCurrentClientRow(self) -> int:
        return self.__client_table.currentRow()

    def GetCurrentUserRow(self) -> int:
        return self.__user_table.currentRow()
    
    def GetTableItem(self, row: int, column: int) -> str:
        return self.__table.item(row, column).text()
    
    def GetClientTableItem(self, row: int, column: int) -> str:
        return self.__client_table.item(row, column).text()
    
    def GetUserTableItem(self, row: int, column: int) -> str:
        return self.__user_table.item(row, column).text()
    
    def GetRowCount(self) -> int:
        return self.__table.rowCount()

    def GetClientRowCount(self) -> int:
        return self.__client_table.rowCount()
    
    def GetUserRowCount(self) -> int:
        return self.__user_table.rowCount()
    
    def ShowTable(self) -> None:
        self.__table.show()

    def ShowControlWidget(self) -> None:
        self.__controls_widget.show()

    def HideLoginWidget(self) -> None:
        self.__login_widget.hide()

    def InsertRow(self) -> None:
        self.__table.insertRow(self.__table.rowCount())

    def InsertClientRow(self) -> None:
        self.__client_table.insertRow(self.__client_table.rowCount())

    def InsertUserRow(self) -> None:
        self.__user_table.insertRow(self.__user_table.rowCount())

    def RemoveRow(self, row: int) -> None:
        self.__table.removeRow(row)
    
    def RemoveClientRow(self, row: int) -> None:
        self.__client_table.removeRow(row)

    def RemoveUserRow(self, row: int) -> None:
        self.__user_table.removeRow(row)

    def GetStartDate(self) -> str:
        return self.__start_date_edit.date().toString("yyyy-MM-dd")
    
    def GetEndDate(self) -> str:
        return self.__end_date_edit.date().toString("yyyy-MM-dd")
    
    def GetClientIdInput(self) -> str:
        return self.__client_id_input.text()

    def __TranslateField(self, selected_texts: dict, line: str):
            return selected_texts.get(line, line)

    def TranslateUI(self):
        lang = self.__language_dropdown.currentText()
        translations = {
            "RO": {
                "Hotel Room Management": "Gestionare camere hotel",
                "Username": "Utilizator",
                "Password": "Parolă",
                "Login": "Autentificare",
                "Show Rooms": "Afișează camere",
                "Add Room": "Adaugă cameră",
                "Update Room": "Actualizează cameră",
                "Delete Room": "Șterge cameră",
                "Location": "Locație",
                "Max Price": "Preț maxim",
                "Position": "Poziție",
                "Facility": "Facilitate",
                "Reserve Room": "Rezervă cameră",
                "Logout": "Deconectare",
                "Client ID": "ID client",
                "Room Management": "Gestionare camere",
                "Client Management": "Gestionare clienți",
                "Statistics": "Statistici",
                "User Management": "Gestionare utilizatori",
                "Client Name": "Nume client",
                "Client Email": "Email client",
                "Client Phone Number": "Telefon client",
                "Add Client": "Adaugă client",
                "Update Client": "Actualizează client",
                "Delete Client": "Șterge client",
                "Show Floors": "Afișează etaje",
                "Show Cities": "Afișează orașe",
                "Save data": "Salvează date",
                "Add User": "Adaugă utilizator",
                "Update User": "Actualizează utilizator",
                "Delete User": "Șterge utilizator",
                "List User": "Listează utilizatori",
                "User ID": "ID utilizator",
                "User Name": "Nume utilizator",
                "User Password": "Parolă utilizator",
                "User Role": "Rol utilizator",
                "You do not have permission to manage users.": "Nu aveți permisiunea să gestionați utilizatorii.",
                "Information": "Informație",
            },
            "EN": {
            },
            "DE": {
                "Hotel Room Management": "Hotelzimmerverwaltung",
                "Username": "Benutzername",
                "Password": "Passwort",
                "Login": "Anmelden",
                "Show Rooms": "Zimmer anzeigen",
                "Add Room": "Zimmer hinzufügen",
                "Update Room": "Zimmer aktualisieren",
                "Delete Room": "Zimmer löschen",
                "Location": "Ort",
                "Max Price": "Maximaler Preis",
                "Position": "Position",
                "Facility": "Ausstattung",
                "Reserve Room": "Zimmer reservieren",
                "Logout": "Abmelden",
                "Client ID": "Kunden-ID",
                "Room Management": "Zimmerverwaltung",
                "Client Management": "Kundenverwaltung",
                "Statistics": "Statistiken",
                "User Management": "Benutzerverwaltung",
                "Client Name": "Kundenname",
                "Client Email": "Kunden-E-Mail",
                "Client Phone Number": "Kundentelefonnummer",
                "Add Client": "Kunde hinzufügen",
                "Update Client": "Kunde aktualisieren",
                "Delete Client": "Kunde löschen",
                "Show Floors": "Stockwerke anzeigen",
                "Show Cities": "Städte anzeigen",
                "Save data": "Daten speichern",
                "Add User": "Benutzer hinzufügen",
                "Update User": "Benutzer aktualisieren",
                "Delete User": "Benutzer löschen",
                "List User": "Benutzer auflisten",
                "User ID": "Benutzer-ID",
                "User Name": "Benutzername",
                "User Password": "Benutzerpasswort",
                "User Role": "Benutzerrolle",
                "You do not have permission to manage users.": "Sie haben keine Berechtigung, Benutzer zu verwalten.",
                "Information": "Information",
            }
        }

        selected_texts: dict = translations.get(lang, {})
  
        self.setWindowTitle(self.__TranslateField(selected_texts, "Hotel Room Management"))
        self.__username_input.setPlaceholderText(self.__TranslateField(selected_texts, "Username"))
        self.__password_input.setPlaceholderText(self.__TranslateField(selected_texts, "Password"))
        self.__login_button.setText(self.__TranslateField(selected_texts, "Login"))
        self.__loc_input.setPlaceholderText(self.__TranslateField(selected_texts, "Location"))
        self.__price_input.setPlaceholderText(self.__TranslateField(selected_texts, "Max Price"))
        self.__pos_input.setPlaceholderText(self.__TranslateField(selected_texts, "Position"))
        self.__fac_input.setPlaceholderText(self.__TranslateField(selected_texts, "Facility"))
        self.__filter_button.setText(self.__TranslateField(selected_texts, "Show Rooms"))
        self.__add_button.setText(self.__TranslateField(selected_texts, "Add Room"))
        self.__update_button.setText(self.__TranslateField(selected_texts, "Update Room"))
        self.__delete_button.setText(self.__TranslateField(selected_texts, "Delete Room"))
        self.__reserve_room_button.setText(self.__TranslateField(selected_texts, "Reserve Room"))
        self.__logout.setText(self.__TranslateField(selected_texts, "Logout"))
        self.__client_id_input.setPlaceholderText(self.__TranslateField(selected_texts, "Client ID"))
        self.__employee_tab_widget.setTabText(0, self.__TranslateField(selected_texts, "Room Management"))
        self.__employee_tab_widget.setTabText(1, self.__TranslateField(selected_texts, "Client Management"))
        self.__employee_tab_widget.setTabText(2, self.__TranslateField(selected_texts, "Statistics"))
        self.__employee_tab_widget.setTabText(3, self.__TranslateField(selected_texts, "User Management"))
        self.__table.setHorizontalHeaderLabels([
            "ID", self.__TranslateField(selected_texts, "Hotel Name"), "Number", self.__TranslateField(selected_texts, "Location"),
            self.__TranslateField(selected_texts, "Price"), self.__TranslateField(selected_texts, "Position"), self.__TranslateField(selected_texts, "Facility") + "s"
        ])
        self.__client_table.setHorizontalHeaderLabels([
            self.__TranslateField(selected_texts, "Client Id"), self.__TranslateField(selected_texts, "Client Name"), self.__TranslateField(selected_texts, "Client Email"), self.__TranslateField(selected_texts, "Client Phone Number")
        ])
        self.__add_client_button.setText(self.__TranslateField(selected_texts, "Add Client"))
        self.__update_client_button.setText(self.__TranslateField(selected_texts, "Update Client"))
        self.__delete_client_button.setText(self.__TranslateField(selected_texts, "Delete Client"))
        self.__show_floors_button.setText(self.__TranslateField(selected_texts, "Show Floors"))
        self.__show_cities_button.setText(self.__TranslateField(selected_texts, "Show Cities"))
        self.__save_data_button.setText(self.__TranslateField(selected_texts, "Save data"))
        self.__user_table.setHorizontalHeaderLabels([
            self.__TranslateField(selected_texts, "User ID"), self.__TranslateField(selected_texts, "User Name"), self.__TranslateField(selected_texts, "User Password"), self.__TranslateField(selected_texts, "User Role")
        ])
        self.__add_user_button.setText(self.__TranslateField(selected_texts, "Add User"))
        self.__update_user_button.setText(self.__TranslateField(selected_texts, "Update User"))
        self.__remove_user_button.setText(self.__TranslateField(selected_texts, "Delete User"))
        self.__list_user_button.setText(self.__TranslateField(selected_texts, "List User"))
        self.__user_tab_message_1.setText(self.__TranslateField(selected_texts, "You do not have permission to manage users."))
        self.__user_tab_message_2.setText(self.__TranslateField(selected_texts, "You do not have permission to manage users."))
        self.__user_tab_message_3.setText(self.__TranslateField(selected_texts, "You do not have permission to manage users."))
        self.__user_tab_message_4.setText(self.__TranslateField(selected_texts, "You do not have permission to manage users."))

    def ShowMessage(self, message: str) -> None:
        lang = self.__language_dropdown.currentText() if hasattr(self, "_UserView__language_dropdown") else "EN"
        translations = {
            "RO": "Informație",
            "EN": "Information",
            "DE": "Information"
        }
        QMessageBox.warning(self, translations.get(lang, "Information"), message)
