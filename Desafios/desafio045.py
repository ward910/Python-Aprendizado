from random import randint
from time import sleep

print("""
Suas opções:

[0] PEDRA
[1] PAPEL
[2] TEROURA
""")

jogador = int(input('Qual é a sua jogada? '))

jokenpo = ('PEDRA', 'PAPEL', 'TEROURA')

computador = randint(0, 2)

print('JO')
sleep(0.7)

print(' KEN')
sleep(0.7)

print('  PÔ!!!', end='\n')
sleep(0.7)

try:
    print('-=' * 18)
    print(f'COMPUTADOR JOGOU {jokenpo[computador]}\nJAGADOR JOGOU {jokenpo[jogador]}')
    print('-=' * 18)
except:
    print('JOGADA INVÁLIDA!!!')
    exit()

# PAPEL

if jokenpo[jogador] == 'PAPEL' and jokenpo[computador] == 'PEDRA':
    print('JOGADOR VENCE')

elif jokenpo[computador] == 'PAPEL' and jokenpo[jogador] == 'PEDRA':
    print('COMPUTADOR VENCE')

elif jokenpo[jogador] == 'PAPEL' and jokenpo[computador] == 'TEROURA':
    print('JOGADOR VENCE')

elif jokenpo[computador] == 'PAPEL' and jokenpo[jogador] == 'TEROURA':
    print('COMPUTADOR VENCE')

# PEDRA

elif jokenpo[jogador] == 'PEDRA' and jokenpo[computador] == 'TEROURA':
    print('JOGADOR VENCE')

elif jokenpo[computador] == 'PEDRA' and jokenpo[jogador] == 'TEROURA':
    print('COMPUTADOR VENCE')

elif jokenpo[jogador] == 'PEDRA' and jokenpo[computador] == 'PAPEL':
    print('JOGADOR VENCE')

elif jokenpo[computador] == 'PEDRA' and jokenpo[jogador] == 'PAPEL':
    print('COMPUTADOR VENCE')

# TEROURA

elif jokenpo[jogador] == 'PEDRA' and jokenpo[computador] == 'TEROURA':
    print('JOGADOR VENCE')

elif jokenpo[computador] == 'PEDRA' and jokenpo[jogador] == 'TEROURA':
    print('COMPUTADOR VENCE')

else:
    print('EMPATE')
