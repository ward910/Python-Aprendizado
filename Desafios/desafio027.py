nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer')

nomeSplit = nome.split()

primeiroNome = nomeSplit[0]
ultimoNome = nomeSplit[-1]

print(f'Seu primeiro nome é {primeiroNome}')
print(f'Seu último nome é {ultimoNome}')