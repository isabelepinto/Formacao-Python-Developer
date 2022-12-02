coluna01 = input().lower()
coluna02 = input().lower()
coluna03 = input().lower()

if coluna01 == 'vertebrado':
  if coluna02 == 'ave':
    if coluna03 == 'carnivoro':
      print('aguia')
    else:
      print('pomba')
  else:
    if coluna03 == 'onivoro':
      print('homem')
    else:
      print('vaca')
else:
  if coluna02 == 'inseto':
    if coluna03 == 'hematofago':
      print('pulga')
    else:
      print('lagarta')
  else:
    if coluna03 == 'hematofago':
      print('sanguessuga')
    else:
      print('minhoca')
      