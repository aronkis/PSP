import os
import sqlite3
import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = "Hotels.db"
db_path = os.path.join(script_dir, db_path).replace("misc","database")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
DROP TABLE IF EXISTS Room;
''')
cursor.execute('''
DROP TABLE IF EXISTS Booking;
''')

cursor.execute('''
DROP TABLE IF EXISTS User;
''')

cursor.execute('''
DROP TABLE IF EXISTS Client;
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_name TEXT,
    number INTEGER,
    location TEXT,
    price REAL,
    position TEXT,
    facilities TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date DATE,
    end_date DATE,
    room_id INTEGER,
    client_id INTEGER,
    FOREIGN KEY (room_id) REFERENCES Room(id),
    FOREIGN KEY (client_id) REFERENCES Client(id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    client_email TEXT,
    client_phone_number TEXT
);
''')

cursor.execute('''
INSERT INTO Room (hotel_name, number, location, price, position, facilities)
VALUES
('Hotel A', 101, 'Paris', 120.5, '1st floor', 'TV, AC, WiFi'),
('Hotel B', 102, 'New York', 200.0, '2nd floor', 'TV, WiFi'),
('Hotel A', 103, 'Paris', 150.0, '1st floor', 'AC, WiFi'),
('Hotel C', 104, 'Tokyo', 180.75, '3rd floor', 'WiFi');
''')

booking_data = [
    (datetime.date(2025, 1, 1).isoformat(), datetime.date(2025, 12, 31).isoformat(), 1, 1),
    (datetime.date(2025, 6, 10).isoformat(), datetime.date(2025, 6, 15).isoformat(), 2, 2),
    (datetime.date(2025, 6, 20).isoformat(), datetime.date(2025, 6, 22).isoformat(), 3, 3)
]
cursor.executemany(
    'INSERT INTO Booking (start_date, end_date, room_id, client_id) VALUES (?, ?, ?, ?);',
    booking_data
)

cursor.execute('''
INSERT INTO Client (client_name, client_email, client_phone_number)
VALUES
('John Doe', 'john@example.com', '+1234567890'),
('Jane Smith', 'jane@example.com', '+0987654321'),
('Emily White', 'emily@example.com', '+1122334455');
''')

cursor.execute('''
INSERT INTO User (username, password, role)
VALUES
('admin', 'password123', 1),
('user1', 'password1', 2),
('user2', 'password2', 2);
''')

conn.commit()

print("Database populated successfully.")

conente_path = "DatabaseContent.txt"
conente_path = os.path.join(script_dir, conente_path)
with open(conente_path, "w") as file:
    print("File Opened")
    file.write("Users (Employees and Administrators):\n")
    file.write("username, password, role\n")
    cursor.execute("SELECT * FROM User")
    for row in cursor.fetchall():
        file.write(f"{row}\n")

    file.write("\nClients (No Password):\n")
    file.write("client_name, client_email, client_phone_number\n")
    cursor.execute("SELECT * FROM Booking")
    for row in cursor.fetchall():
        file.write(f"{row}\n")

    file.write("\nBookings:\n")
    file.write("start_date, end_date, room_id, client_id\n")
    cursor.execute("SELECT * FROM Booking")
    for row in cursor.fetchall():
        file.write(f"{row}\n")
 
    file.write("\nRooms:\n")
    file.write("hotel_name, number, location, price, position, facilities\n")
    cursor.execute("SELECT * FROM Room")
    for row in cursor.fetchall():
        file.write(f"{row}\n")

conn.close()

print("\nDatabase setup complete and data inserted!")
