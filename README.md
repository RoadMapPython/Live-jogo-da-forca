# Live-jogo-da-forca
## Código com o jogo da forca , um readme para mais detalhes e o link do video da live :D 






from random import choice
import os
import colorama

with open('Aplicacoes.txt') as aplicacoes:
    linhas=aplicacoes.read()
    list= linhas.split('\n')
palavra= choice(list).lower()

acertos = 0
erros = 0
erroletra = ''
acertoletra = ''

while acertos != len(palavra) and erros != 6:

    print(' ')
    
    mensagem = ''
    
    for letra in palavra:
    
        if letra in acertoletra:
            mensagem += f'{letra}'
        else:
            mensagem += '_'
    print(mensagem)
    print('No momento')
    print("Tentativas restantes:", 6 - erros)
    print('Erros : ', erroletra)
    print('Acertos :  ', acertoletra)
    letra=str(input('Digite a letra:').lower())

    os.system("cls")
    if letra in acertoletra or letra in erroletra:
        print('Ops você ja usou essa letra')
    elif letra.isalpha() == False:
        print('Você não digitou uma letra!')
    elif letra in palavra:
        print('Tem essa letra uau !')
        acertoletra += letra
        acertos += palavra.count(letra)
    else:
        print('Uma pena , não tem essa letra')
        erroletra += letra
        erros += 1
print('fim')
