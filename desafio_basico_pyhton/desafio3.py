n = int(input(""))

while(n > 0):
  numeros = str(input())
  lista_numeros = numeros.split()
  a = lista_numeros[0]
  b = lista_numeros[1]
  if b == (a[(len(a)-len(b)):]):
    print('encaixa')
  else:
    print('nao encaixa')
  n -= 1


# #4
# # 56234523485723854755454545478690 78690
# # 5434554 543
# # 1243 1243
# # 54 64545454545454545454545454545454554