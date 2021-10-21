# Live-jogo-da-forca
## Código com o jogo da forca , um readme para mais detalhes e o link da live gravada: YouTube: https://youtu.be/RqSXq9Yfd7o 
######Obs: tem um dicionário de palavras no final do documento

===============================|Introdução|==================================<br />
* *Olá sejam bem vindos(as) a nossa 4° Live do nosso projeto de RoadMapPython, hoje iremos realizar a criação de um jogo da forca em python , utilizando  o Atom como editor de  * *texto executando o python via terminal, ao decorrer da criação do código vou explicar mais como funciona.

* *Primeiramente eu queria conversar sobre o que é um jogo da forca e como consiste ele .Bem , o jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra que   * *foi dada, a pessoa deve tentar acertar chutando as letras , caso acerte a pessoa ganha , mas caso a pessoa chute várias letras que estejam erradas o usuário perde.
* *E é quase isso que iremos realizar hoje so que em formato de código, iremos pegar o que acabamos de falar e deixar aqui 
* *destacado para lembrarmos do objetivo de nosso código de hoje.

* *Na live de hoje iremos utilizar bastante o conceito de listas durante a construção do código ,listas e tuplas podem conter vários valores, o que torna mais fácil escrever    * *programas que lidam com grandes quantidades de dados. E como as próprias listas podem conter outras listas, você pode usá-las para organizar os dados em cadeias de comandos.

=========================|Como executar o código via terminal|===================================<br />
Para executar o código é facil , só você saber aonde ele está localizado o meu por exemplo está na área de trabalho 
da pastas Live jogo da forca que está dentro da pasta roadmap python , o cmd por padrão já inicia com seu usuárioda máquina,
como por exemplo C:\Users\Juan> e para chegar ate ao local que está nosso código é so utilizar um comando em shell para , 
irmos até la .

cd Desktop\Roadmap Python\Live jogo da forca

Ai pronto estamos na pasta , agora é so digitar python JogoDaForca.py que executa o código ,simples ne?

===========================|Construção do código|====================================<br />
Agora que demos uma passada no conceito de listas iremos direto ao código , vamo declarar uma váriavel.
  
  escolha ='Roadmap'
    
a palavra 'Roadmap' está armazenada na variável escolha

agora vamos fazer o usuário tentar adivinhar uma letra 

letra=input('Digite a letra:')
if letra in escolha:
     print('Você acertou uma letra')
else :
     print('Você errou uma letra')

pronto! agora nosso usuário pode ver se tem uma etra na palavra

=====================================================================================<br />
 Ta mas e agora? O código vai ficar assim mesmo so uma letrinha ?
 iremos resolver isso agora utilizando o while 
 
acertos = 0
erros   = 0
escolha='Roadmap'.lower()

while acertos != len(escolha) and erros != 6:

  letra=input('Digite a letra:').lower()
  if letra in escolha:
       print('Você acertou uma letra')
       acertos += 1
  else :
       print('Você errou uma letra')
       erros += 1
 O while é uma estrutura de repetição então enquanto acertos for diferente do numero de letras 
 da palavra escolhida ou errar 6 letras que não estão na palavra
 
 enquanto o usuário acertar ou errar vai indo acumulando dentro dessas váriaveis como por exemplo ,
 o acertos += 1 , é basicamente acertos=acertos+1 o total de acertos vai contar mais 1, e esse novo 
 número vai passar a ser o total de acertos , o mesmo para o erro , que quando o usuário errar vai ,
 somar mais um na variável de erro dele.
 
====================================================================================<br />
"Nossa mas eu coloquei vários A e consegui ganhar !?", é isso que iremos resolver agora!

acertos = 0
erros   = 0
acertoletra = ' '
erroletra = ' '

escolha='Roadmap'.lower()

while acertos != len(escolha) and erros != 6:
  letra=input('Digite a letra:').lower()
  
  if letra in acertoletra or letra in erroletra:
       print('Ops você ja usou essa letra ʘ.ʘ')
  
  elif letra.isalpha() == False:
       print('Você não digitou uma letra! ◉.◉')
       
  elif letra in escolha:
       print('Você acertou uma letra')
       acertoletra += letra
       acertos += 1
       
  else :
       print('Você errou uma letra')
       erroletra += letra
       erros += 1
       
 Primeiro adicionamos listas vazias para colocarmos variaveis dentro,
 e colocamos dentro do elif de acertos e no else de erros acumulando as
 letras que a pessoa errou ou acertou, após isso adicionamos um if e um elif ,
 para verificar se a pessoa ja digitou uma letra ou se a pessoa não digitou uma letra.
 
 '''
   if letra in acertoletra or letra in erroletra:
       print('Ops você ja usou essa letra ʘ.ʘ')
  
  elif letra.isalpha() == False:
       print('Você não digitou uma letra! ◉.◉')
 '''
=========================================================================================<br />
Sim agora não posso digitar a mesma letra ou digitar uma coisa que nao seja do alfabeto
so que tem palavra com letra repetida o que eu faço?

========================================================================================<br />
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

=======================================================================================<br />

agora iremos fazer um for no nosso jogo da forca

   for letra in palavra:
aqui estamos pegando cada letra da palavra e retornando dentro da estrutura abaixo
   if letra in acertoletra:
           mensagem += letra
 
   else:
            mensagem += '_'
se não estiver iremos imprimir os tracinhos que escondem as letras no jogo da forca, e que será 
mostrado no código abaixo
======================================================================================<br />
Na live não foi abordado de inicio o conceito de colorama , mas iremos introduzir .
   
   for letra in escolha:
   if letra in acertoletra:
        mensagem += letra             
    else:
        mensagem += '_'           
    print(mensagem)
    print(mensagem)
    print(Fore.GREEN + Style.BRIGHT + "ıllı No momento ıllı" )
    print(Fore.CYAN+"Tentativas restantes:", 6 - erros  )
    print(Fore.RED +'Erros : ', erroletra )
    print(Fore.BLUE + 'Acertos :  ', acertoletra  )
    print(Fore.CYAN)
    letra=str(input('Digite a letra:').lower())
    
Nessa parte do código foi feito o que será mostrada ao usuário.

======================================|Código completo|==========================================<br />
Obs: O código abaixo pode não estar com a identação correta.

    from random import choice
    import os
    import colorama
    from colorama import Fore
    from colorama import Style

    colorama.init()

    with open('Aplicacoes.txt') as aplicacoes:

       linhas=aplicacoes.read()
       list= linhas.split('\n')
    escolha= choice(list).lower()

    acertos = 0
    erros = 0
    erroletra = ''
    acertoletra = ''

    while acertos != len(escolha) and erros != 6:

        print(' ')
    
        mensagem = ''
    
        for letra in escolha:
    
           if letra in acertoletra:
               mensagem += letra             
            else:
               mensagem += '_'           
        print(mensagem)
    print(Fore.GREEN + Style.BRIGHT + "ıllı No momento ıllı" )
    print(Fore.CYAN+"Tentativas restantes:", 6 - erros  )
    print(Fore.RED +'Erros : ', erroletra )
    print(Fore.BLUE + 'Acertos :  ', acertoletra  )
    print(Fore.CYAN)
    letra=str(input('Digite a letra:').lower())

    os.system("cls")
    if letra in acertoletra or letra in erroletra:
        print(Fore.RED + 'Ops você ja usou essa letra ʘ.ʘ')
    elif letra.isalpha() == False:
        print('Você não digitou uma letra! ◉.◉')
    elif letra in escolha:
        print('Tem essa letra uau ! ツ ')
        acertoletra += letra
        acertos += escolha.count(letra)
    else:
        print('Uma pena , não tem essa letra x _ x')
        erroletra += letra
        erros += 1
    os.system("cls")
    if erros == 6:
       print(Fore.RED + Style.BRIGHT +'(x ╭╮ x) Game Over (x ╭╮ x)',Style.RESET_ALL)

    elif acertos == len(escolha):
        print(Fore.GREEN + Style.BRIGHT + "^.^ Você ganhou, parabens! ^.^ " + Style.RESET_ALL)
       
-_-_-Dicionário-_-_-<b>
From      A partir de<b>
random    Aleatório(a)
choice    Escolha
import    Importar
Fore      Parte da frente do texto
Style     Estilo 
init      Iniciar
with      Com
open      Abrir
split     Dividir
lower     Diminuir
while     Enquanto
for       Para
if        E se
else      Senão
RESET_ALL Resetar tudo
