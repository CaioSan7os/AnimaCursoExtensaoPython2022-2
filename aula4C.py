#importar a biblioteca sqlite3
import sqlite3


#2 e 3 VIRA função conectar()
def conectar():
  #Vamos estabelecer uma conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

#criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor
