from time import sleep

print('=' * 10 + ' Lojas Guanabara ' + '=' * 10)

preco = float(input('Preço da compras: R$'))
sleep(0.20)

print('FORMAS DE PAGAMENTO')
print("""
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
""")

option = int(input('Qual é a opção? '))


if option == 1:
    por = 10 / 100
    valor_final = preco - (por * preco)
elif option == 2:
    por = 5 / 100
    valor_final = preco - (por * preco)
elif option == 3: 
    valor_final = preco
elif option == 4:
    por = 20 / 100
    valor_final = preco + (por * preco)

    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será pracelas {parcelas:.2f}x de R${valor_final / parcelas:.2f} COM JUROS')
    print(f'Sua compra de {preco:.2f} vai custar R${valor_final:.2f} no final.')
    exit()
else:
    print('OPÇÃO INVALIDA')

print(f'Sua compra de R${preco:.2f} vai custar R${valor_final:.2f}')



