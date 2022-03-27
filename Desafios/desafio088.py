from random import randint
from time import sleep

print('-'*35)
print('	JOGA NA MEGA SENA')
print('-'*35)

listaDeNumero = []; numSorteio = []; num = [-1]
numDeVezes = int(input('Quantos jogo quer que eu sorteie? '))
print()

for c in range(0, numDeVezes):
	for i in range(1, 6+1):
		random = randint(1, 60)
		if len(numSorteio) >= 1:
			if len(num) > 0:
				if num.count(random) >= 1:
					randomNovo = randint(1, 60)
					while True:
						randomNovo = randint(1, 60)
						
						if randomNovo != random:
							break
					
					random = randomNovo
		numSorteio.append(random)
		num.append(random)
	
	if len(numSorteio) >= 7:
		numSorteio.pop()
	numSorteio.sort()
	listaDeNumero.append(numSorteio)
	print(f'Jogo {c+1}: {listaDeNumero[c]}')
	numSorteio.clear()
	num.clear()
	sleep(0.25)
