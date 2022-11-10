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