soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite {} número: '.format(c)))
    if n % 2 == 0:
        soma += num
        cont += 1

print('-' * 10)
print(f'Você informou {cont} números pares e a soma foi {soma}')
print('-' * 10)