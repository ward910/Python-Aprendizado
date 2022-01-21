print('Geredor de PA')
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
total = 10
pa = termo; cont = 0

while True:
    while cont <= total:
        print(pa, end=' -> ')
        pa += razao
        cont += 1
    if cont >= total:
        print('PAUSA')
        novosTermos = int(input('Quantos termos você quer mostrar a mais? '))
        if novosTermos == 0:
            print(f'Progressão finalizada com {cont - 1} termos mostrados')
            exit()

        total += novosTermos
       