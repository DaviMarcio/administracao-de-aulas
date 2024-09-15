import sqlite3
import tkinter as tk
from tkinter import ttk


con = sqlite3.connect("Alunos.db")
cur = con.cursor()

cur.execute("CREATE TABLE  IF NOT EXISTS alunos(nome TEXT NOT NULL, instrumento TEXT NOT NULL, nível TEXT NOT NULL)")

con.commit()
con.close()

def inserir_valores(nome, instrumento, nível):
  con = sqlite3.connect("Alunos.db")
  cur = con.cursor()
  cur.execute("""INSERT INTO alunos (nome, instrumento, nível) VALUES (?, ?, ?)""", (nome, instrumento, nível))
  con.commit()
  con.close()

def salvar_valores():
  nome = entry.get().strip()
  instrumento = instrumento_cb.get()
  nivel = nivel_cb.get()

  if nome and instrumento and nivel:
    inserir_valores(nome, instrumento, nivel)
    status_label.config(text="Aluno adicionado")
  else:
    status_label.config(text="Preencha todos os campos")
window = tk.Tk()
window.title('Administração de Aulas')
window.geometry('600x400+50+50')
window.iconbitmap('./app.ico')


nome_label = tk.Label(text="Nome do Aluno")
entry = tk.Entry()

instrumento_label = tk.Label(text="Instrumento que toca") 
instrumento_cb = ttk.Combobox(window)

instrumento_cb['values'] = ('Guitarra', 'Violão', 'Bateria', 'Teclado', 'Contrabaixo', 'Ukulele', 'Cavaquinho')
instrumento_cb['state'] = 'readonly'

nivel_label = tk.Label(text="Nível do Aluno") 
nivel_cb = ttk.Combobox(window)

nivel_cb['values'] = ('Iniciante', 'Intermediário', 'Avançado')
nivel_cb['state'] = 'readonly'

botao = tk.Button(window, text="Adicionar Aluno", command= salvar_valores)



nome_label.pack()

entry.pack()

instrumento_label.pack()

instrumento_cb.pack()

nivel_label.pack()

nivel_cb.pack()

botao.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()

