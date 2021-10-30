from colorama import Fore, Style

num = int(input('Qual é a velocidade do carro? '))

if num > 80:
    kmExcedente = num - 80 
    multaValor = float(7) * kmExcedente
    print(f'{Fore.RED}MULTADO! Você excedeu o limite permitido que é de 80km/h{Style.RESET_ALL}')
    print(f'{Fore.RED}Você deve pagar uma multar de{Style.RESET_ALL}{Fore.GREEN} R${multaValor:.2f}!{Style.RESET_ALL}')

print(f'{Fore.GREEN}Tenha um bom dia! Dirija em seguranção!{Style.RESET_ALL}')
