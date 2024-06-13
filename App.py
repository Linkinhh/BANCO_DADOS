from tkinter import *
import oracledb
import getpass
import tkinter

# ---------------------------
connection = oracledb.connect(user="a15390310", password="a15390310", dsn="orclgrad1.icmc.usp.br/pdb_elaine.icmc.usp.br", port=1521)
print("Feita a conexao.")

cursor = connection.cursor()
cursor.execute("select * from SISTEMA")
result = cursor.fetchall()

# ---------------------------

root = tkinter.Tk()
root.title("BANCO DE DADOS")
root.config(background="white")

pushLoginInterface(root)

left_frame = Frame(root, width=400, height=400)
left_frame.grid(row=1, column=1, padx=0, pady=5)

contador = 0
for i in result:
    textinho = str(i)
    Label(left_frame, text=textinho).grid(row=contador, column=0, padx=5, pady=5)
    contador += 1    

root.mainloop()