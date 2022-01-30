cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n < 999:
        soma += n
        cont += 1
    else:
        print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
        exit()
