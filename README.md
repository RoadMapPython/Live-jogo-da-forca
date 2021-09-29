# Live-jogo-da-forca
## Código com o jogo da forca , um readme para mais detalhes e o link do video da live :D 

==============================================================================================================
Agora chegamos em uma parte que parece complicada , mas quando for entendida você vai pensar "Agora eu entendi
,agora eu saquei ,agora todas as peças encaixaram!"  

with open('Aplicacoes.txt') as aplicacoes:
basicamente estamos abrindo um arquivo que é o Aplicacoes.txt e chamando ele de 
aplicacoes
    linhas=aplicacoes.read()
aqui estamos lendo o arquivo
    list= linhas.split('\n')
vai pegar as linhas e separar por \n ,e pegar cada elemento separarando 
ele por quebras de linha que é o '\n'
palavra= choice(list).lower()
o choice está aqui basicamente para escolher uma palavra aleatória dentro da variavel 
list

==============================================================================================================

agora iremos fazer um for no nosso jogo da forca

    for letra in palavra:
aqui estamos pegando cada letra da palavra e retornando dentro da estrutura abaixo
    if letra in acertoletra:
            mensagem += letra
 
    else:
            mensagem += '_'
se não estiver iremos imprimir 


==============================================================================================================
