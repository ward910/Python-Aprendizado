from random import randint

numeroSorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os  valores sorteados foram: {numeroSorteio}')

print(f'O maior valor sorteado foi {max(numeroSorteio)}')
print(f'O menor valor sorteado foi {min(numeroSorteio)}')
        


