TecladoInput = input('Digite algo: ')
print(f'O tipo primetivo desse valor é {type(TecladoInput)}')
print(f'Só tem espaços? {TecladoInput.isspace()}')
print(f'É um número? {TecladoInput.isnumeric()}')
print(f'É alfabético? {TecladoInput.isalpha()}')
print(f'É alfanúmerico? {TecladoInput.isalnum()}')
print(f'Está em maiúsculas? {TecladoInput.isupper()}')
print(f'Está em minúculas? {TecladoInput.islower()}')
print(f'Está capitalizada? {TecladoInput.istitle()}')