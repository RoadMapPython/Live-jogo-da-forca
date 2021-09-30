# Live-jogo-da-forca
## Código com o jogo da forca , um readme para mais detalhes e o link da live gravada :D 

Olá sejam bem vindos a nossa 4° Live do nosso projeto de RoadMapPython, hoje iremos realizar a criação de um jogo da forca em python , utilizando o atom como nosso bloco de notas :3 , e utilizando o cmd como compilador .
Primeiramente eu queria conversar sobre o que é um jogo da forca e como consiste ele .Bem , o jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra que foi dada, a pessoa deve tentar acertar chutando as letras , caso acerte a pessoa ganha , mas caso a pessoa chute várias letras que estejam erradas o usuário perde.
E é quase isso que iremos realizar hoje so que em formato de código, iremos pegar o que acabamos de falar e deixar aqui destacado para lembrarmos do objetivo de nosso código de hoje.
Na live de hoje iremos utilizar bastante o conceito de listas durante a construção do código ,listas e tuplas podem conter vários valores, o que torna mais fácil escrever programas que lidam com grandes quantidades de dados. E como as próprias listas podem conter outras listas, você pode usá-las para organizar os dados em estruturas hierárquicas.
==============================================================================================================
Agora chegamos em uma parte que parece complicada ,que é um conteudo que nao é abordado na disciplina do técnico ,um pouco complexo mais usado em conteúdos mais avançados ,porém entretanto todavia iremos fazer uma breve pincelada para o entendimento dessa estrutura ,mas pode deixar que quando for entendida você vai pensar "Agora eu entendi
,agora eu saquei ,agora todas as peças encaixaram!"  

with open('Aplicacoes.txt') as aplicacoes:

basicamente estamos abrindo um arquivo que é o Aplicacoes.txt e chamando ele de 
aplicacoes

    linhas=aplicacoes.read()
    
aqui estamos lendo o arquivo "Aplicacoes.txt" que agora está dentro da variável "aplicacoes"

    list= linhas.split('\n')

aqui vai pegar as linhas e separar(split) por \n ,e pegar cada elemento separarando 
ele por quebras de linha.

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
===================================|Código completo|=======================================
