from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)

numRandom = randint(0, 5)

num = int(input('Em que número eu pensei? '))

print('\033[1;37m{}'.format('PROCESSANDO...'))

sleep(2)

if num == numRandom:
    print('\033[1;32m{} \033[1;42m'.format('PARÁBENS! Você conseguiu me vencer!'))
else:
    print('\033[1;31m{} {} {} {} \033[1;41m'.format('GANHEI! Eu pensei no número', numRandom, 'e não no', num))
