import sqlite3
from datetime import datetime

DATABASE = "notes.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_all_notes(search=None, category=None):
    conn = get_db()
    query = "SELECT * FROM notes"
    params = []
    if search:
        query += " WHERE title LIKE ? OR content LIKE ?"
        params.extend([f"%{search}%", f"%{search}%"])
    if category:
        query += " AND category = ?" if "WHERE" in query else " WHERE category = ?"
        params.append(category)
    notes = conn.execute(query, params).fetchall()
    conn.close()
    return notes

def get_note(id):
    conn = get_db()
    note = conn.execute("SELECT * FROM notes WHERE id=?", (id,)).fetchone()
    conn.close()
    return note

def create_note(title, content, category):
    conn = get_db()
    conn.execute(
        "INSERT INTO notes (title, content, category) VALUES (?,?,?)",
        (title, content, category)
    )
    conn.commit()
    conn.close()

def update_note(id, title, content, category):
    conn = get_db()
    conn.execute(
        "UPDATE notes SET title=?, content=?, category=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
        (title, content, category, id)
    )
    conn.commit()
    conn.close()

def delete_note(id):
    conn = get_db()
    conn.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()
