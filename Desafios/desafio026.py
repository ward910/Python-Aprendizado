frase = str(input('Digite uma frase: ')).strip()

fraseUpper = frase.upper()

print(f'A letra aparece {fraseUpper.count("A")} vezes na frase')
print(f'A primeira letra A apareceu na posição {fraseUpper.find("A") + 1}')
print(f'A última letra A apareceu na apareceu na posição {fraseUpper.rfind("A") + 1}')