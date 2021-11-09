from datetime import date

ano = int(input('Que ano quer analisa? Coloque 0 pra analisar o ano atual: '))

def testeBissexto(testeAno):
    if (testeAno % 4 == 0 and testeAno % 100 != 0) or (testeAno % 400 == 0):
        return f'O ano {testeAno} é BISSEXTO'
    else: 
        return f'O ano {testeAno} NÃO é BISSEXTO'

if ano == 0:
    data = date.today()
    anoAtual = int(data.strftime("%Y"))
    print(testeBissexto(anoAtual))
else:
    print(testeBissexto(ano))