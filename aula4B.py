#importar a biblioteca sqlite3
import sqlite3

#Vamos estabelece uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#criar um objeto do tipo cursor
cursor = conexao.cursor()

#comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#Executar o comando SQL
cursor.execute(sql)

#Confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()
