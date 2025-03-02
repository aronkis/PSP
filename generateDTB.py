import sqlite3

conn = sqlite3.connect('hotel_management.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotels (
        hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        num_rooms INTEGER NOT NULL
    )
''')

def create_room_table(hotel_name):
    table_name = hotel_name.replace(" ", "_").lower()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER NOT NULL,
            floor_number INTEGER NOT NULL,
            price_per_night REAL NOT NULL,
            room_type TEXT NOT NULL
        )
    ''')

def insert_hotel_data(name, location, num_rooms):
    cursor.execute('''
        INSERT INTO hotels (name, location, num_rooms)
        VALUES (?, ?, ?)
    ''', (name, location, num_rooms))
    conn.commit()

    create_room_table(name)

    table_name = name.replace(" ", "_").lower()
    for room_number in range(1, num_rooms + 1):
        floor_number = (room_number - 1) // 2 + 1  
        price_per_night = 100 + (room_number * 10)  
        room_type = 'Single' if room_number % 2 == 0 else 'Double'

        cursor.execute(f'''
            INSERT INTO {table_name} (room_number, floor_number, price_per_night, room_type)
            VALUES (?, ?, ?, ?)
        ''', (room_number, floor_number, price_per_night, room_type))

    conn.commit()

hotels = [
    ("Grand Plaza", "New York", 10),
    ("Seaside Resort", "California", 10),
    ("Mountain View Inn", "Colorado", 10),
    ("Lakeside Hotel", "Michigan", 10),
    ("City Center Hotel", "Chicago", 10)
]

for hotel in hotels:
    insert_hotel_data(hotel[0], hotel[1], hotel[2])

conn.close()
