import sqlite3
import os

DB_NAME = "data/fitns_pro.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            weight REAL,
            height REAL,
            age INTEGER,
            goal TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            exercise TEXT,
            series INTEGER,
            reps INTEGER,
            load REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nutrition_log(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            food TEXT,
            calories REAL,
            protein REAL,
            carbs REAL,
            fat REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_log(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            quantity_ml REAL
        )
    """)
    conn.commit()
    conn.close()

create_tables()
