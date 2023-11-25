import sqlite3 as lite  
con = lite.connect( 'dados.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE categoria(ID INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT)")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE receitas(ID INTEGER PRIMARY KEY AUTOINCREMENT,categoria TEXT, adicionado_em DATE, valor DECIMAL)") 

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(ID INTEGER PRIMARY KEY AUTOINCREMENT,categoria TEXT, adicionado_em DATE, valor DECIMAL)") 