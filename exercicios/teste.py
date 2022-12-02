def mensagem():
  print('Bom dia')


def carro(nome: str, marca: str, valor: float, ano: int):
  print(f'Carro inserido com sucesso! {nome.title()}/{marca.title()}/{valor:.2f}/{ano}')


mensagem()
carro('palio', 'fiat', 2500, 1998)
carro()