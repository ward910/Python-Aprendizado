from datetime import date

anoNascimento = int(input('Ano de nascimento: '))

ano_atual = date.today()

anoIdade = ano_atual.year - anoNascimento 

anoAlistamento = 18 - anoIdade   

print(f'Quem nasceu em {anoNascimento} tem {anoIdade} em {ano_atual.year}')

if anoIdade < 18:
    print(f'Ainda faldam {anoAlistamento} anos para o alitamento')
    print(f'Seu alistamento será em {anoAlistamento + ano_atual.year}')
elif anoIdade > 18:
    print(f'Você já deveria ter se alistamento há {anoIdade - 18}')
    print(f'Seu alistamento foi em {ano_atual.year - (anoIdade - 18)}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

