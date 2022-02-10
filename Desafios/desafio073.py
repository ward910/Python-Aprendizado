tabelaTimes = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians',
'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo')

print('='*40)

print('Lista do brasileirão: ', tabelaTimes)
print('='*40)

print('Os cinco primeiros são: ', tabelaTimes[:6])
print('='*40)

print('Os quarto últimos são: ', tabelaTimes[-4:])

print('='*40)

print('Times em ordem alfábetica', sorted(tabelaTimes))
print('='*40)

print(f"O Corinthians está na {tabelaTimes.index('Corinthians') + 1}ª posisão")
