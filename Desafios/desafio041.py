from datetime import date

data_atual = date.today()

anoNascimento =  int(input('Ano de Nascimento: '))

idadeNadador = data_atual.year - anoNascimento

print(f'O atleta tem {idadeNadador}')

if idadeNadador <= 9:
    print('Classificação: MIRIM')

elif idadeNadador > 9 and idadeNadador <= 14:
    print('Classificação: INFANTIL')

elif idadeNadador > 14 and idadeNadador <= 19:
    print('Classificação: JÚNIOR')

elif idadeNadador > 19 and idadeNadador <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')