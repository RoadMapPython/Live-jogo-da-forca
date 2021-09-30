from random import choice
import os
import colorama
from colorama import Fore
from colorama import init

colorama.init()

with open('Aplicacoes.txt') as aplicacoes:
    linhas=aplicacoes.read()
    list=linhas.split('\n')
escolha=choice(list).lower()

acertos=0
erros=0
acertoletra=''
erroletra=''

while acertos != len(escolha) and erros != 6:
    print(' ')
    mensagem=''

    for letra in escolha:
        if letra in acertoletra:
            mensagem += letra
        else:
            mensagem += '_'

    print(mensagem)
    print(Fore.GREEN + "ıllıNo momentoıllı")
    print(Fore.CYAN + "Tentativas restantes:",  6 - erros)
    print(Fore.RED + "Erros:", erroletra)
    print(Fore.GREEN + "Acertos:", acertoletra)
    print(Fore.CYAN)
    letra=input('Digite uma letra:').lower()

    os.system('cls')

    if letra in acertoletra or letra in erroletra:
        print('Ops essa letra ja tem ʘ.ʘ')

    elif letra.isalpha() == False:
        print('Uai isso não é uma letra ◉.◉')

    elif letra in escolha:
        print(Fore.GREEN + 'Tem essa letra uau! ツ')
        acertoletra += letra
        acertos += 1


    else:
        print(Fore.RED + 'Infelizmente não tem essa letra x _ x')
        erroletra += letra
        erros += 1

os.system('cls')
if erros == 6:
    print(Fore.RED + '(x ╭╮ x) Game over (x ╭╮ x)')
elif acertos == len(escolha):
    print(Fore.GREEN + 'Parabéns você acertou era: ', escolha)
