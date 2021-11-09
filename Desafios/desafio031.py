viagemKm = int(input('Qual é a distância da sua viagem? '))

def res(Kmviagem, res):
    print(f'Você está prestes a começar uma viagem de {Kmviagem}Km')
    print(f'E o preço da sua passagem será de R${res:.2f}')

if viagemKm <= 200:
    resultado = (50/100) * viagemKm
    res(viagemKm, resultado)
else:
    resultado = (45/100) * viagemKm
    res(viagemKm, resultado)
    