while True:
    tab = int(input('Quer ver tabuada de qual valor? ')); fat = 1
    if tab > 0:
        while fat != 11:
            print(f'{tab} x {fat} = {tab * fat}')
            fat += 1
    else:
        print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
        exit()
