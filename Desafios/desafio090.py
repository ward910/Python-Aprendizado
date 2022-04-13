nome = str(input('Nome: '))
media = float(input('Média de {}: '.format(nome)))
dados = {}

dados['nome'] = nome
dados['media'] = media

if dados['media'] >= 7:
	dados['situaçao'] = 'Aprovado'
elif dados['media'] >= 5:
	dados['situaçao'] = 'Recuperação'
else:
	dados['situaçao'] = 'Reprovado'

print('-=' * 30)
for k, v in dados.items():
	print(f'  - {k} é igual {v}')
