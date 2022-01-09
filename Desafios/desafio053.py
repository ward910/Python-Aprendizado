frase = str(input('Digite a frase: ')).replace(" ", "").upper()

fraseInvertidar = frase[::-1]

print(f'O inverso de {frase} é {fraseInvertidar}') 

if fraseInvertidar == frase:
    print('Temos um palíndromo')
else:
    print('NÃO temos um palídromo')