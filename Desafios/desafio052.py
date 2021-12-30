n = int(input('Digite o número: '))

tot = 0

for cont in range(1, n + 1):
    if n % cont == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    
    print(f'{cont}', end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')

if tot == 2:
    print('E por isso que ele é PRIMO')
else:
    print('E por isso que ele NÃO é PRIMO')