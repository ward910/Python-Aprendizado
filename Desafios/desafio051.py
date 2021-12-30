print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)

primeiroTermo = int(input('Primero termo: '))
razao = int(input('Razão: '))
n = 10

ultimo = primeiroTermo + n*razao

for pa in range(primeiroTermo, ultimo, razao):
    print(pa, end=' ==> ')

print('ACABOU')