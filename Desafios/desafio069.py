print('-'*30); print('CADASTRE UMA PESSOA'); print('-'*30)

listaM = []; listaF = []

# Entrada de dados
while True:
	idade = int(input('Idade: '))
	
	sexo = ' '
	while sexo.upper() not in 'MF':
		sexo = str(input('Sexo [M/F] ')).strip().upper()[0]

	if sexo == 'M':
		listaM.append(idade)
	else:
		listaF.append(idade)

	continuar = ' '
	while continuar not in 'SN':
		continuar = str(input('Que continuar? [S/N] ')).strip().upper()[0]

	if continuar == 'N':
		break

# Análise de dados
contT = contF = contM = 0

for x in listaF:
	if x < 18:
		contT += 1

	if x < 20:
		contF += 1

for x in listaM:
	if x < 18:
		contT += 1
	contM += 1

 
print(f'Total de pessoas com menos de 18 anos: {contT}')
print(f'Ao todo temos {contM} homens cadastrados')
print(f'E temos {contF} mulheres com menos de 20 anos')
