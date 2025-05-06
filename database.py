import sqlite3

def conectar():
    return sqlite3.connect("notas.db")

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            fornecedor TEXT NOT NULL,
            data TEXT NOT NULL,
            valor REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_nota(numero, fornecedor, data, valor):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO notas (numero, fornecedor, data, valor) VALUES (?, ?, ?, ?)",
              (numero, fornecedor, data, valor))
    conn.commit()
    conn.close()

def listar_notas():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM notas")
    notas = c.fetchall()
    conn.close()
    return notas
