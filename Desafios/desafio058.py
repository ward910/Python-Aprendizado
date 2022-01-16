from random import randint

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

numeroAleatorio = randint(0, 10)
cont = 0
while True:
    n = int(input('Qual é seu papite? '))
    if n == numeroAleatorio:
        cont += 1
        break
    elif numeroAleatorio > n:
        cont += 1
        print('Mais... Tente mais uma vez.')
    else:
        cont += 1
        print('Menos... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas. Parabéns!')
