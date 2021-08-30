from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
sino = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {sino:.2f}')
consseno = cos(radians(an))
print(f'O ângulo de {an} tem o CONSSENO de {consseno:.2f}')
tangente = tan(radians(an))
print(f'O ângulo de {an} tem o TANGENTE de {tangente:.2f}')
