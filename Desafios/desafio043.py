peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) ')) 

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')  