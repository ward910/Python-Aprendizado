from time import sleep
from random import randint
from operator import itemgetter

jogadores = {}
ranking = {}
print('Valores sorteados: ')

for c in range(1, 4+1):
	num = randint(1, 6)
	jogadores['jogador{}'.format(c)] = num
	
	print(f'jogador{c} tirou {num} no dado.')
	sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == RANKING DOS JOGADORES ==')

c = 1
for i, v in enumerate(ranking):
	print(f' {c}° lugar: {v[0]} :: {v[1]}')
	c += 1

