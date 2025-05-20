from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox
)
from PyQt5.QtCore import Qt

class ClientView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Room Lister")
        self.Init_ui()
    
    def Init_ui(self) -> None:
        self.__layout = QVBoxLayout()
        self.client_tab = QWidget()
        self.__client_widget = QWidget()
        __client_layout = QVBoxLayout()

        self.__language_dropdown = QComboBox()
        self.__language_dropdown.addItems(["EN", "RO", "DE"])
        self.__language_dropdown.setFixedWidth(60)
        self.__language_dropdown.currentIndexChanged.connect(self.TranslateUI)
        self.__layout.addWidget(self.__language_dropdown)

        self.__client_table = QTableWidget()
        self.__client_table.setColumnCount(7)
        self.__client_table.setHorizontalHeaderLabels([
            "ID", "Hotel Name", "Number", "Location", "Price", "Position", "Facilities"
        ])
        self.__client_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        
        __client_filter_layout = QHBoxLayout()
        self.__client_loc_input = QLineEdit()
        self.__client_loc_input.setPlaceholderText("Location")
        self.__client_price_input = QLineEdit()
        self.__client_price_input.setPlaceholderText("Max Price")
        self.__client_pos_input = QLineEdit()
        self.__client_pos_input.setPlaceholderText("Position")
        self.__client_fac_input = QLineEdit()
        self.__client_fac_input.setPlaceholderText("Facility")
        self.__client_filter_button = QPushButton("Show Rooms")
        __client_filter_layout.addWidget(self.__client_loc_input)
        __client_filter_layout.addWidget(self.__client_price_input)
        __client_filter_layout.addWidget(self.__client_pos_input)
        __client_filter_layout.addWidget(self.__client_fac_input)
        __client_filter_layout.addWidget(self.__client_filter_button)

        __client_layout.addLayout(__client_filter_layout)

        self.__login_button_c = QPushButton("Login")
        login_button_layout = QHBoxLayout()
        login_button_layout.addStretch(1)
        login_button_layout.addWidget(self.__login_button_c)
        login_button_layout.addStretch(1)
        __client_layout.addLayout(login_button_layout)

        self.__client_widget.setLayout(__client_layout)

        client_tab_layout = QVBoxLayout()
        client_tab_layout.addWidget(self.__client_table)
        client_tab_layout.addWidget(self.__client_widget)
        self.__layout.addLayout(client_tab_layout)
        self.setLayout(self.__layout)

        self.TranslateUI()

    def Update(self, rooms: list[list[str]]) -> None:
        self.__client_table.setRowCount(len(rooms))
        for row_idx, room in enumerate(rooms):
            for col_idx, value in enumerate(room):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.__client_table.setItem(row_idx, col_idx, item)
    
    def GetLocationInputClient(self) -> str:
        return self.__client_loc_input.text()

    def GetPriceInputClient(self) -> str:
        return self.__client_price_input.text()

    def GetPositionInputClient(self) -> str:
        return self.__client_pos_input.text()

    def GetFacilitiesInputClient(self) -> str:
        return self.__client_fac_input.text()
    
    def SetFilterFunctionClient(self, callback: callable) -> None:
        self.__client_filter_button.clicked.connect(callback)
    
    def SetLoginFunctionClient(self, callback: callable) -> None:
        self.__login_button_c.clicked.connect(callback)
    
    def __TranslateField(self, selected_texts: dict, line: str):
        return selected_texts.get(line, line)

    def TranslateUI(self):
        lang = self.__language_dropdown.currentText()
        translations = {
            "RO": {
                "Room Lister": "Listă camere",
                "Login": "Autentificare",
                "Show Rooms": "Afișează camere",
                "Location": "Locație",
                "Max Price": "Preț maxim",
                "Position": "Poziție",
                "Facility": "Facilitate",
                "ID": "ID",
                "Hotel Name": "Nume hotel",
                "Number": "Număr",
                "Price": "Preț",
                "Facilities": "Facilități"
            },
            "EN": {},
            "DE": {
                "Room Lister": "Zimmerliste",
                "Login": "Anmelden",
                "Show Rooms": "Zimmer anzeigen",
                "Location": "Ort",
                "Max Price": "Maximaler Preis",
                "Position": "Position",
                "Facility": "Ausstattung",
                "ID": "ID",
                "Hotel Name": "Hotelname",
                "Number": "Nummer",
                "Price": "Preis",
                "Facilities": "Ausstattungen"
            }
        }
        selected_texts: dict = translations.get(lang, {})

        self.setWindowTitle(self.__TranslateField(selected_texts, "Room Lister"))
        self.__client_loc_input.setPlaceholderText(self.__TranslateField(selected_texts, "Location"))
        self.__client_price_input.setPlaceholderText(self.__TranslateField(selected_texts, "Max Price"))
        self.__client_pos_input.setPlaceholderText(self.__TranslateField(selected_texts, "Position"))
        self.__client_fac_input.setPlaceholderText(self.__TranslateField(selected_texts, "Facility"))
        self.__client_filter_button.setText(self.__TranslateField(selected_texts, "Show Rooms"))
        self.__login_button_c.setText(self.__TranslateField(selected_texts, "Login"))
        self.__client_table.setHorizontalHeaderLabels([
            self.__TranslateField(selected_texts, "ID"),
            self.__TranslateField(selected_texts, "Hotel Name"),
            self.__TranslateField(selected_texts, "Number"),
            self.__TranslateField(selected_texts, "Location"),
            self.__TranslateField(selected_texts, "Price"),
            self.__TranslateField(selected_texts, "Position"),
            self.__TranslateField(selected_texts, "Facilities")
        ])
