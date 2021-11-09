from colorama import Fore, Style

num = int(input(f'{Fore.BLUE}Me diga um número qualquer: {Style.RESET_ALL}'))

if num % 2 == 0:
    print(f'O número {num} é {Fore.BLUE}PAR!{Style.RESET_ALL}')
else:
    print(f'O número {num} é {Fore.BLUE}IMPAR!{Style.RESET_ALL}')