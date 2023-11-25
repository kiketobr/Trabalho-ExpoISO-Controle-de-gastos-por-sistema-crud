import sqlite3 as lite  
con = lite.connect( 'dados.db')
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM categoria WHERE nome ='aluguel'")
