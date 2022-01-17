from time import sleep


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while True:
    print(' [ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior\n [ 4 ] novos números\n [ 5 ] sair do programa')
    opcao = int(input('>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')

    if opcao == 2:
        mul = n1 * n2
        print(f'o resultado entre {n1} * {n2} é {mul}')

    if opcao == 3:
        if n1 == n2:
            print('Os valores são iguais')
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        if n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')

    if opcao == 4:
        novoN1 = int(input('Primeiro valor: '))
        novoN2 = int(input('Segundo valor: '))

        n1 = novoN1; n2 = novoN2
    if opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa! Volte sempre!')
        exit()
    
    if opcao != 1 != 2 != 3 != 4 != 5:
        print('Opção inválida. Tente novamente')
    print('-=' * 12)
        