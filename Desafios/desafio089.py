listaDeAlunos = []
aluno = 0

while True:
	nome = str(input('Nome: '))
	nota01 = float(input('Nota 1: '))
	nota02 = float(input('Nota 2: ')) 
	media = (nota01 + nota02) / 2
	listaDeAlunos.append([nome, [nota01, nota02], media])
	
	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
	
	if continuar == 'N':
		break

print('-='*30)
print('No. NOME MÉDIA')
print('-'*26)
for i in range(0, len(listaDeAlunos)):
		print(i, listaDeAlunos[i][0], f'{listaDeAlunos[i][2]:.2}')
print('-'*26)

while True:
	aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
	
	if aluno == 999:
		exit()
	for c in range(0, len(listaDeAlunos)):
		if c == aluno:
			print(f'As notas do aluno {listaDeAlunos[aluno][0]} são {listaDeAlunos[aluno][1]}')

