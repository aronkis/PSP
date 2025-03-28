import os
import sqlite3
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = "Hotels.db"
db_path = os.path.join(script_dir, db_path).replace("misc","database")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Administrator', 'Employee'))
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT NOT NULL UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INTEGER,
    number INTEGER NOT NULL,
    location TEXT NOT NULL,
    price REAL NOT NULL,
    available BOOLEAN NOT NULL,
    facilities TEXT,
    FOREIGN KEY (hotel_id) REFERENCES hotels(id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    room_id INTEGER,
    booking_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Confirmed', 'Cancelled')),
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
''')

users = [
    ('admin_user', 'admin@example.com', 'adminpassword', 'Administrator'),
    ('employee1', 'employee1@example.com', 'password123', 'Employee'),
    ('employee2', 'employee2@example.com', 'password123', 'Employee')
]
cursor.executemany('''
INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?);
''', users)

hotels = [
    ('Grand Hotel', 'New York'),
    ('Sea View Inn', 'Miami'),
    ('Mountain Retreat', 'Denver')
]
cursor.executemany('''
INSERT INTO hotels (name, location) VALUES (?, ?);
''', hotels)

def get_hotel_ids():
    cursor.execute('SELECT id FROM hotels;')
    return [row[0] for row in cursor.fetchall()]

hotel_ids = get_hotel_ids()

room_data = []
room_count = 5 
for hotel_id in range(1, 4):
    for i in range(1, room_count + 1):  
        random_floor = i 
        room_number =  random_floor * 100 + i
        room_location = f"Floor {random_floor}"
        room_price = 100 + (i * 20)
        room_available = True
        facilities = "WiFi, TV, AC"
        room_data.append((hotel_id, room_number, room_location, room_price, room_available, facilities))

cursor.executemany('INSERT INTO rooms (hotel_id, number, location, price, available, facilities) VALUES (?, ?, ?, ?, ?, ?)', room_data)

clients = [
    ('John Doe', 'john.doe@example.com', '1234567890'),
    ('Jane Smith', 'jane.smith@example.com', '0987654321'),
    ('Bob Johnson', 'bob.johnson@example.com', '1122334455'),
    ('Alice Brown', 'alice.brown@example.com', '5566778899'),
    ('Tom White', 'tom.white@example.com', '6677889900')
]
cursor.executemany('''
INSERT INTO clients (name, email, phone_number) VALUES (?, ?, ?);
''', clients)

def get_client_ids():
    cursor.execute('SELECT id FROM clients;')
    return [row[0] for row in cursor.fetchall()]

def get_room_ids():
    cursor.execute('SELECT id FROM rooms;')
    return [row[0] for row in cursor.fetchall()]

client_ids = get_client_ids()
room_ids = get_room_ids()

bookings = []
for client_id in client_ids:
    bookings.append((client_id, room_ids.pop(0), datetime.now().strftime('%Y-%m-%d'), 'Confirmed'))
    bookings.append((client_id, room_ids.pop(0), datetime.now().strftime('%Y-%m-%d'), 'Pending'))

cursor.executemany('''
INSERT INTO bookings (client_id, room_id, booking_date, status) VALUES (?, ?, ?, ?);
''', bookings)

conn.commit()

print("Database populated successfully.")

def show_data():
    conente_path = "DatabaseContent.txt"
    conente_path = os.path.join(script_dir, conente_path)
    with open(conente_path, "w") as file:
        print("File Opened")
        file.write("Users (Employees and Administrators):\n")
        file.write("id, username, email, password, role\n")
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            file.write(f"{row}\n")

        file.write("\nClients (No Password):\n")
        file.write("id, name, email\n")
        cursor.execute("SELECT * FROM clients")
        for row in cursor.fetchall():
            file.write(f"{row}\n")

        file.write("\nHotels:\n")
        file.write("id, name, location\n")
        cursor.execute("SELECT * FROM hotels")
        for row in cursor.fetchall():
            file.write(f"{row}\n")

        file.write("\nRooms:\n")
        file.write("id, hotel_id, room_number, location, price, available, facilities\n")
        cursor.execute("SELECT * FROM rooms")
        for row in cursor.fetchall():
            file.write(f"{row}\n")

        file.write("\nBookings:\n")
        file.write("id, client_id, hotel_id, booking_date, status\n")
        cursor.execute("SELECT * FROM bookings")
        for row in cursor.fetchall():
            file.write(f"{row}\n")
            
show_data()

conn.close()

print("\nDatabase setup complete and data inserted!")
