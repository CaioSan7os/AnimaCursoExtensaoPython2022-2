#input() solicita um input do usuario
# variaveis "nome" e "idade"
#print() output de dados/ exibe dados armazenados

nome = input("digite seu nome: ")
idade = int (input ("digite sua idade: "))
print(f"o seu nome é {nome} e você tem {idade} anos de idade. :)")
print("seja bem vindo {0}, você tem {1} anos, logo ja é maior de idade".format(nome, idade))
print(f"o dobro da sua idade é {idade*2}")