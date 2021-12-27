tabuada = int(input('Digite um número para ver sua tabuada: '))

res = 1
print('-----------')
for c in range(1, 11):
      print(f'{tabuada} x {res} = {tabuada * res}')
      res = c + 1
print('-----------')