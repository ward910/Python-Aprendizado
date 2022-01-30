media = cont = maior = menor = 0; numeros = []
while True:
    numero = int(input('Digite um número: ')); numeros.append(numero);cont += 1; menor = numero
    opecao = str(input('Quer continuar? [S/N] '))
    if opecao.upper() != 'S':  
        for i in range(len(numeros)):
            media += numeros[i]
            if cont == 1:
                maior = menor = numero
            else:     
                if numeros[i] > maior:
                    maior = numeros[i]
                if numeros[i] < menor:
                    menor = numeros[i]

        print(f'Você digitou {cont} números e a média foi {media/2}')
        print(f'O maior valor foi {maior} e o menor foi {menor}')
        exit()