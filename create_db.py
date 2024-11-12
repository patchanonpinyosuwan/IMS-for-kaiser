import sqlite3

def create_db():
    # เชื่อมต่อกับฐานข้อมูล
    conn = sqlite3.connect('ims.db')
    cursor = conn.cursor()

    # สร้างตาราง Supplier (ถ้ายังไม่มี)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        contact TEXT,
        email TEXT,
        address TEXT,
        product TEXT,
        supply_date TEXT
    )
    ''')

    # สร้างตาราง customer (ถ้ายังไม่มี)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        name TEXT,
        contact TEXT,
        email TEXT,
        address TEXT
    )
    ''')

    # สร้างตาราง employee (ถ้ายังไม่มี)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        utype TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        pass TEXT,
        address TEXT,
        salary TEXT,
        doj TEXT
    )
    ''')

    # สร้างตาราง product (ถ้ายังไม่มี)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER,
        price REAL,
        status TEXT
    )
    ''')

    # คอมมิทการเปลี่ยนแปลงและปิดการเชื่อมต่อ
    conn.commit()
    conn.close()

# เรียกฟังก์ชัน create_db เพื่อสร้างตาราง
create_db()
