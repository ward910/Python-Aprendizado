n = int(input('Quantos termos você quer mostrar? '))

cont = 3
u = 0
p = 0 + 1

print(0, end=' -> ')
while cont <= n:
    termo = p + u
    p = u
    u = termo

    print(termo, end=' -> ')
    
    cont += 1

print('FIM')