salario = float(input('Qual é o salário do Funcionário? R$'))
aumentoSalario = salario + (salario * (5 / 100))

print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${aumentoSalario:.2f}')