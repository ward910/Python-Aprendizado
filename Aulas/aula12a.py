nome = str(input('Qual é seu nome? '))

if nome == "Vinicius":
    print('Que nome bonito!')

elif nome == 'Vanessa' or nome == 'Nicolas' or nome == 'Ana':
    print('Seu nome é popular no Brasil')

elif nome in 'Ana Juliana Carlos':
    print('Belo nome feminino')  
else: 
    print('Que nome normal!')
print(f'Bom dia, {nome}')