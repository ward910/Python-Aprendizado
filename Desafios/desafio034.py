funSalario = int(input('Qual é o salário do funcionário? R$'))

if funSalario >= 1250:
    por = int(((funSalario / 100) * 10) + funSalario)
else:
    por = int(((funSalario / 100) * 15) + funSalario)

print(f'Quem ganhava {funSalario} passa a ganhar {por} agora.')