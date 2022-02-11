parCont = 0 
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')) )

print(f'Você digitou os valores {num}')
for c in num:
    if c % 2 == 0:
        parCont += 1

print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
