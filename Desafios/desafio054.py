from datetime import date

pessoas = []
for i in range(1, 8):
    pessoa = str(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    pessoas += pessoa.split()

ma = 0; me = 0
for p in range(0, 7):
    ano =  date.today().year - int(pessoas[p])

    if ano >= 21:
        ma += 1
    else:
        me += 1

print(f'Ao todo tivemos {ma} pessoas de maiores de idade')
print(f'E também tivemos {me} pessoas menores de idade')