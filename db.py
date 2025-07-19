import sqlite3

DB_NAME = "clients.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_clients():
    conn = get_connection()
    clients = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    return clients

def get_client(phone):
    conn = get_connection()
    client = conn.execute("SELECT * FROM clients WHERE phone = ?", (phone,)).fetchone()
    conn.close()
    return dict(client) if client else None

def add_client(name, phone, status, notes):
    conn = get_connection()
    conn.execute("INSERT INTO clients (name, phone, status, notes) VALUES (?, ?, ?, ?)",
                 (name, phone, status, notes))
    conn.commit()
    conn.close()

def update_client(phone, name, status, notes):
    conn = get_connection()
    conn.execute("UPDATE clients SET name = ?, status = ?, notes = ? WHERE phone = ?",
                 (name, status, notes, phone))
    conn.commit()
    conn.close()
