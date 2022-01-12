nomes = []
idades = []
sexos = []
for pessoa in range(1, 5):
    print(f'----- {pessoa}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    nomes.append(nome); idades.append(idade); sexos.append(sexo)

idadeTotal = 0
maiorIdade = 0
nomePessoaMaisVelha = None
quantedadeMulheres = 0

for i in range(0, 3):
    idadeTotal = idadeTotal + idades[i]

for i in range(0, 3):
    if sexos[i] == 'M':
        if i == 0:
            maiorIdade = idades[i]
            nomePessoaMaisVelha = nomes[i]
        else:
            if idades[i] > maiorIdade:
                maiorIdade = idades[i]
                nomePessoaMaisVelha = nomes[i]

for i in range(0, 3):
    if sexos[i] == 'F':
        if idades[i] < 20:
            quantedadeMulheres += 1 

print(f'A média de idade do grupo é de {idadeTotal / 2} anos')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomePessoaMaisVelha}.')
print(f'Ao todo são {quantedadeMulheres} mulheres com menos de 20 anos')