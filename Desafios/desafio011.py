larg = float(input('Lagura da parade: '))
altu = float(input('Altura da parade: '))

area = larg * altu
tinta = area / 2

print(f'Sua parede tem a dimensão {larg}x{altu} e tem a area {area}m²')
print(f'Para pintar essa parede você precisará de {tinta:.1f}l de tinta')