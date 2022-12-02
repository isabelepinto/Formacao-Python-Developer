#calcular a energia dos seres vivos
#se maior que 8000, gritar “Mais de 8000!”, se nao gritar "Inseto!"

def energia_seres_vivos(repeticao):
  for i in range(0, repeticao):
    energia = int(input('Qual a energia desse ser vivo? '))
    if 100 <= energia <= 100000:
      if energia <= 8000:
        print('Inseto!')
      else:
        print('Mais de 8000!')


repeticao = int(input('Quantos seres vivos quer analisar? '))
energia_seres_vivos(repeticao)
