from random import randint

print('='*30);print('VAMOS JOGAR PAR OU ÍMPAR');print('='*30)
cont = 0
res = ''

while True:
	n = int(input('Diga um número: ')) 
	computador = randint(0, 10)
	total = n + computador
	jogadorPI = str(input('PAR ou IMPAR? [P/I] '.upper())) 
	computadorPI = 'P'
	
	if jogadorPI == 'I':
		computadorPI = 'P'
	else: 
		computadorPI = 'I'

	if n <= 10 and n > 0:
		
		if total % 2 == 0:
			res = 'PAR'
		else: 
			res = 'IMPAR'

		print('-'*30); print(f'Você jogou {n} e o computador {computador}. Total de {n + computador} DEU {res}'); print('-'*30)

		if res[0] == jogadorPI:
			print('Você VENCEU!! \nVamos jogar novamente')
			print('='*30)
			cont += 1
		else:
			print('Você PERDEU!!')
			print('='*30)
			
			print(f'GAME OVER!! Você VENCEU {cont} vezes')
			exit()
