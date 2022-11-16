print("funções")


def calcular_imposto(preco_produto):
  imposto = preco_produto * .05
  return imposto

preco = 299
imposto = calcular_imposto(preco)
print(imposto)

valores = [12.32, 32.43, 54.42, 3232.34]
for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto(valor)}")
#Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#se imposto for 10%
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")