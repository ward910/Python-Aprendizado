print('-=' * 20)
print('Analisador de triângulo')
print('-=' * 20)

a = float(input('Primeiro segemento: '))
b = float(input('Segundo segemento: '))
c = float(input('Terceiro segemento: '))

if a + b > c and a + c > b and b + c > a:

    print('Os segementos PORDEM FORMAR um triângulo!')
else:
    print('Os segementos NÃO PORDEM FORMAR um triângulo!')