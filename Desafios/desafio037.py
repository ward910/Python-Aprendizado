n = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] coverter para OCTAL\n[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO e igual a {:b}'.format(n, n))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {:o}'.format(n, n))
else:
    print('{} convertido para HEXADECIMAL e igual a {:x}'.format(n, n))