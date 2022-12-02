def meu_amor(nome, *data, **musica):
  msc = '\n'.join([f'{chave.title()} - {valor.title()}' for chave, valor in musica.items()])
  print(f"""
O nome dela é {nome} e ela me encantou.
Nossas datas são: 
  {data[0]}, quando nos beijamos a primeira vez
  E dia {data[1]}, quando começamos a namorar.
Algumas de nossas músicas são: 
  {msc}
  """)


meu_amor('Ana Carolina', '07 de Agosto', '10 de Setembro', nina = 'Naíse', caetano = 'Deusa Urbana', afroito = 'perco tudo')
