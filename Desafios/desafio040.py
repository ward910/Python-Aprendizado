n1 = float(input('Primeira nota: '))
n2 = float(input('Segundo nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média do aluno é {media}')

if media < 5:
    print('O aluno REPROVADO')
elif media < 6.9:
    print('O aluno RECUPERAÇÃO')
elif media > 7:
    print('O aluno APROVADO')
