numerosEx = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))

while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print('Você digito o número', numerosEx[n])

