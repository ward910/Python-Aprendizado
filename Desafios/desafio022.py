nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem o todo {len(nome) - nome.count(" ")}')

nomeSplit = nome.split()

print(f'Seu primero nome é {nomeSplit[0][0:]} e ele tem {len(nomeSplit[0][0:])} letras')