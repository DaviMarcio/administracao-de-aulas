import sqlite3

con = sqlite3.connect('Alunos.db')
cur = con.cursor()

consulta = f"SELECT * FROM alunos "

cur.execute(consulta)

registros = cur.fetchall()

for registro in registros:
    print(registro)

con.close()


