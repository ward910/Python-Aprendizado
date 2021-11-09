p = int(input('Primeiro número: '))
s = int(input('Segundo número: '))
t = int(input('Treceiro número: '))

# MENOR
menor = p
if p < s:
    menor = s
if s < t:
    menor = t

print(f'O menor valor digitado foi {menor}')

# MAIOR
maior = p
if p > s:
    maior = s
if s > t:
    maior = t

print(f'O maior valor digitado foi {maior}')