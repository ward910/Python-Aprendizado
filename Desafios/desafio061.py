print('Geredor de PA')
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))

pa = termo; cont = 0 

while cont != 10:
    print(pa, end=' -> ')
    pa += razao; cont += 1

print('FIM')
