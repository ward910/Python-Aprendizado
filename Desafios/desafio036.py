casaValor = float(input('Valor da casa? R$'))
salarioComprador = int(input('Seu salario? R$'))
anosPagar = int(input('Quantos anos você vai pagar? '))

anosParaMeses = 12 * anosPagar
valorPrestacao = casaValor / anosParaMeses
salarioPorcentagem = int((30 / 100) * salarioComprador)

print(f'Para uma casa de R${casaValor} em {anosPagar} anos a prestação será de R${valorPrestacao:.2f}')

if valorPrestacao >= salarioPorcentagem:
    print('Empréstimo NEGADO!')    
elif valorPrestacao <= salarioPorcentagem:
    print('Empréstimo pode ser CONCEDIDO!')


