def menu():
  menu =(f'''
{'='*16}MENU{'='*16}
Escolha a ação que deseja realizar:
  [c] - cadastrar cliente
  [n] - nova conta corrente
  [d] - depósito
  [s] - saque
  [e] - extrato
  [0] - sair

{'='*36}

->> ''')

  return input(menu).lower()


#funcao deposito com argumentos por position only
def depositar(saldo, valor, extrato,/):
  #deposito - somente valores positivos | devem ser armazenados em extrato
  if valor <= 0:
    print('Permitido depositar somente valores positivos')
  else:
    saldo += valor
    extrato += f'Depósito de R${valor:.2f}.\n'
    print(f'Depósito realizado com sucesso. \nSeu saldo atual é de R${saldo:.2f}')
  
  return saldo, extrato


#funcao de saque com argumentos keyword only
def sacar(*,saldo, valor, numero_saques, extrato, limite_saque):
  #saque - permitido somente 3 saques por dia | limite por saque = R$ 500,00 | devem ser armazenados em extrato
  #caso o usuário não tenha saldo suficiente, exigir uma mensagem "saldo insuficiente"
  if numero_saques < limite_saque:
    if valor > saldo:
      print('Saldo insuficiente.')
    else:
      if valor > 500:
        print('Limite de saque R$500')
      else:
        saldo -= valor 
        extrato += f'Saque de R${valor:.2f}.\n'
        print(f'Saque realizado com sucesso.\nSeu saldo atual é de R${saldo:.2f}.')
        numero_saques += 1    
  else:
    print('Não pode ultrapassar o limite de 3 saques diários.')

  
  return extrato, saldo, numero_saques


#funcao extrato com argumentos position only and keyword only
def exibir_extrato(saldo,/,*,extrato):

  # lista de todos os saques e depósitos realizados | exibir saldo atual | valores devem ser exibidos com R$ e 2 casas decimais 
  # se o extrato estiver em branco exibir "não foram realizadas transações"  
  if extrato == '':
    print(f'''
{'='*15}EXTRATO{'='*15}

Nenhuma transação foi realizada.

{'='*37}
      ''')

  else:
    print(f'''
{'='*15}EXTRATO{'='*15}
{extrato}\n\n
Saldo final: R${saldo:.2f}
{'='*37}\n\n\n''')


#funao para cadastrar novo usuario
def cadastrar_usuario(usuarios):
  #usuarios devem ser armazenados em uma lista 
  #deve ter: nome, cpf, data de nascimento e endereço- é uma str com formado: logradouro, nº - bairro - cidade/sigla estado
  #cpf deve conter somente numeros - nao podemos cadastrar 2 usuarios com mesmo cpf
  cpf = input('Digite seu CPF(somente número): ')
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print('Já existe usuário com esse cpf')
    return
  
  nome = input('Informe seu nome completo: ')
  data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa)')
  endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/estado)')

  usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço' : endereco})

  print('Usuário cadastrado com sucesso!')



def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
  #declarando constantes
  LIMITE_SAQUES = 3
  AGENCIA = '0001'
  
  #declarando variaveis
  saldo = 0
  numero_saques = 0
  extrato = ''
  usuarios = []
  numero_contas = []

  #iniciando sistema
  print('Olá, seja muito bem-vinde!')

  while True:
    resposta = menu()

    if resposta == 'd':
      valor = float(input('Qual valor deseja depositar? '))

      saldo, extrato = depositar(saldo, valor, extrato)
      
    elif resposta == 's':
      valor = float(input('Qual valor deseja sacar? '))

      extrato, saldo, numero_saques = sacar(saldo = saldo, valor = valor, numero_saques = numero_saques, extrato = extrato, limite_saque = LIMITE_SAQUES)

    elif resposta == 'e':
      exibir_extrato(saldo, extrato = extrato)
    
    elif resposta == 'c':
      cadastrar_usuario(usuarios)
    
    elif resposta == 'n':
      numero_contas = len(contas) + 1
      


    elif resposta == '0':
      print('Obrigada, volte sempre!')
      break

    else:
      print('A resposta digitada é invalida.')

main()