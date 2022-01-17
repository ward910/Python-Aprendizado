from math import factorial

n = int(input('Digite um número para\ncalcular seu Fatorial: '))
print(f'Calculando {n}! = ', end='')
cont = n
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1

print(factorial(n))