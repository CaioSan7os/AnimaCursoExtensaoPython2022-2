#input() solicita um input do usuario
# variaveis "nome" e "idade"
#print() output de dados/ exibe dados armazenados

#nome = input("digite seu nome: ")
#idade = int (input ("digite sua idade: "))
#print(f"o seu nome é {nome} e você tem {idade} anos de idade. :)")
#print("seja bem vindo {0}, você tem {1} anos, logo ja é maior de idade".format(nome, idade))
#print(f"o dobro da sua idade é {idade*2}")
#===================================================
# condicionais em Python
#nome = input("digite seu nome: ")
#idade = int (input ("digite sua idade: "))

#if idade >= 18:
 # print("você é maior de idade, pode dirigir ou beber")
#else:
#  print("você é menor, volta a estudar")
#================================================

genero = input("digite seu genêro de nascimento, sendo M = masculino e F para feminino: ")
idade = int(input("digite sua idade? "))

if genero == "M" and idade >= 18:
  print("você deve se alistar")
elif genero == "M" and idade <= 18:
  print(f"você ainda é menor de idade, falta {18 - idade} ano(s) para se tornar obrigatorio o seu alistamento.")
elif genero == "F":
  print("você não é obrigado a se alistar")
else:
  print("por favor, digite seu genêro de nascimento")