from math import hypot

ca = float(input('Digite cateto adjacente: '))
co = float(input('Digie cateto oposto: '))


print(f'A Hipotenusa é {hypot(ca, co):.2f}')