import sqlite3
import hashlib

def conectar():
    return sqlite3.connect("users.db")

def crear_tabla():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar(user, password):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?)", (user, hash_pass(password)))
    conn.commit()
    conn.close()

def login(user, password):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (user, hash_pass(password)))
    data = c.fetchone()
    conn.close()
    return data
