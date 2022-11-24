#criar menu com opções para o cliente
print('Olá, seja muito bem-vinde!')
menu =('''
Escolha a ação que deseja realizar:
[d] - depósito
[s] - saque
[e] - extrato
[0] - sair

= ''')

#variaveis
saldo = 0
saque = 0
limite_saques = 3
contador_saques = 0
valor_maximo_saque = 500
lista_depositos = []
lista_saques = []


while True:
  #exibir menu e ler opcao escolhi
  opcao = input(menu).lower()

  if opcao == 'd':
    #deposito - somente valores positivos | devem ser armazenados em extrato
    deposito = float(input("Qual valor deseja depositar? \nR$ "))
    if deposito > 0:
      print(f'Depósito de R$ {deposito:.2f} realizado com sucesso.\n')
      lista_depositos.append(deposito)
      saldo = saldo + deposito
      print(f'Saldo final: R${saldo:.2f}\n')
    else:
      print('Depósito não realizado.\nSó é possível realizar depósitos de valores positivos.\n')

  elif opcao == 's':
    #saque - permitido somente 3 saques por dia | limite por saque = R$ 500,00 | devem ser armazenados em extrato
    #caso o usuário não tenha saldo suficiente, exigir uma mensagem "saldo insuficiente"
    if contador_saques < 4:
      saque = float(input('Qual valor deseja sacar? \nR$ '))
      if saque <= 500:
        if saque > saldo:
          print(f'Não podemos realizar seu saque por saldo insuficiente.\nSeu saldo é de R${saldo:.2f}.\n')
        elif saque < 0:
          print('Só é possível realizar saques de valores positivos.\n')
        else:
          print(f'Saque no valor de R${saque:.2f} realizado com sucesso.\n')
          lista_saques.append(saque)
          saldo = saldo - saque
          print(f'Saldo final: R${saldo:.2f}\n')
          contador_saques += 1
      else:
        print('Não podemos realizar seu saque. \nO valor máximo por saque é de R$500,00.\n')
    else:
      print('Não podemos realizar seu saque.\nVocê já realizou seu limite de 3 saques diários.\n')

  elif opcao == "e":
    # lista de todos os saques e depósitos realizados | exibir saldo atual | valores devem ser exibidos com R$ e 2 casas decimais 
    # se o extrato estiver em branco exibir "não foram realizadas transações"
    print(f'''
    Saques realizados: 
      {lista_saques}

    Depósitos realizadods:
      {lista_depositos}

    Saldo final: R${saldo}
    ''')

  elif opcao == "0":
    #digitar opcao 0 sairá do sistema
    print('\nObrigada! Volte sempre :) \n\n')
    break

  else:
    #em caso de algum erro de entrada do usuário
    print('Infelizmente a opção que você digitou está inválida, tente novamente.\n\n')
