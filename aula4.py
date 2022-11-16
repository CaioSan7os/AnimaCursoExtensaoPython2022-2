#importa a biblioteca
import sqlite3
# conexao = sqlite3.connect (conecta com o banco de dados)
conexao = sqlite3.connect("dc_universe.db")
#criar um objeto do tipo cursor
cursor = conexao.cursor()
#comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"
# executar o comando SQL no cursor (SQLite)
cursor.execute(sql)
#exibir a consulta do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"nome({pessoa[1]} {pessoa[3]})")