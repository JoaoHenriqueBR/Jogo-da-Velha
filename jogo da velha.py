# Das bibliotecas os e time, é importado os comandos (system, sleep).
from os import system # system('clear') é usado para limpar a tela.
from time import sleep # sleep(segundos) é usado para pausar o programa.
from random import randint # Biblioteca usada pela cpu para criar suas jogadas.

# Declaração de variáveis
resp = 's'
o = 0
x = 0
v = 0

while resp == 's': # Inicia o jogo.
    # Declaração de variáveis (Dentro do loop, para o usuário poder iniciar outro jogo)
    s1=' '
    s2=' '
    s3=' '
    s4=' '
    s5=' '
    s6=' '
    s7=' '
    s8=' '
    s9=' '
    i = 3 # Importante, é usada para contar o número de jogadas e a vez do jogador.
    status = 'erro'
    modo = 0

    while modo != 1 and modo != 2:
        print('~=~'*5)
        print('JOGO DA VELHA! ')
        print('~=~'*5)
        print('1 - JOGAR CONTRA CPU!')
        print('2 - JOGAR CONTRA AMIGO!')
        try:
            modo = int(input('Escolha o modo de jogo: '))
        except:
            print('\nValor Inválido! Tente Novamente...')
            sleep(2)
        system('clear')
    
    while status == 'erro': # Pequeno loop para decidir a peça inicial.
        p = ['X', 'O'] # lista de peças
        p1 = input('Escolha X ou O: ').upper().strip() # peça inicial escolhida pelo usuário
        if p1 != 'O' and p1 != 'X':
            print('Seleção de peça errada!')
            print('Tente Novamente! ')
            sleep(2)
        else:
            p.remove(p1) # remove a peça inicial da lista de peças
            p2 = p[0] # Da lista, é escolhida a peça que falta para ser segundária
            status = 'ok' # Loop realizado com sucesso, código pode prosseguir...
        system('clear')    
    
    
    lista = [s1, s2, s3, s4, s5, s6, s7, s8, s9] # Lista de posições.

    while i < 12: # A partir desse loop, o jogo começa de verdade, é printado o jogo na tela e o usuário precisa escolher onde colocar a peça.
        print(f'     |     |     ')
        print(f'  {s1}  |  {s2}  |  {s3}  ')
        print(f'     |     |     ')
        print(f'-----+-----+-----')
        print(f'     |     |     ')
        print(f'  {s4}  |  {s5}  |  {s6}  ')
        print(f'     |     |     ')
        print(f'-----+-----+-----')
        print(f'     |     |     ')
        print(f'  {s7}  |  {s8}  |  {s9}  ')
        print(f'     |     |     ')
        print('\n')
    
        
        op = i % 2 # Decide quem é a vez. 
        if op == 1: # Impar é o jogador inicial
            try:
                pos = int(input(f'Peça {p1} escolha uma posição de 1 a 9 no tabuleiro: ')) # Tenta perguntar ao jogador um número de 0 a 10.
            except: # Se ocorrer um erro (Por exemplo digitar letras ou escrever um número decimal):
                pos = 10 # Invalida a posição.
            pesc = p1
        else: # Par é o jogador segundário.
            if modo == 2:
                try:
                    pos = int(input(f'Peça {p2} escolha uma posição de 1 a 9 no tabuleiro: '))
                except:
                    pos = 10
            else:
                cpu = randint(1, 9)
                pos = cpu   
            pesc = p2
        
        if pos < 10 and pos > 0: # Se a posição for válida (Entre 1 e 9)
            if lista[pos-1] != ' ': # Verifica se já foi usada
                if modo == 2:
                    system('clear')
                    print('Essa posição ja está preenchida!')
                    sleep(3)
            else:
                lista[pos-1] = pesc # Peça é registradada na posição escolhida
                # Variáveis recebem seus valores da lista
                s1 = lista[0]
                s2 = lista[1]
                s3 = lista[2]
                s4 = lista[3]
                s5 = lista[4]
                s6 = lista[5]
                s7 = lista[6]
                s8 = lista[7]
                s9 = lista[8]
                i += 1 # Ao fim da jogada, ela é contabilizada.
        else: # Se for inválida, o jogador é avisado.
            system('clear')
            print('Posição errada, tente novamente!')
            sleep(3)
        system('clear')

        # Mostra a jogada na tela
        if s1 == 'X' and s2 == 'X' and s3 == 'X' or s4 == 'X' and s5 == 'X' and s6 == 'X' or s7 == 'X' and s8 == 'X' and s9 == 'X' or s1 == 'X' and s4 == 'X' and s7 == 'X' or s2 == 'X' and s5 == 'X' and s8 == 'X' or s3 == 'X' and s6 == 'X' and s9 == 'X' or s1 == 'X' and s5 == 'X' and s9 == 'X' or s3 == 'X' and s5 == 'X' and s7 == 'X':
            print(f'     |     |     ')
            print(f'  {s1}  |  {s2}  |  {s3}  ')
            print(f'     |     |     ')
            print(f'-----+-----+-----')
            print(f'     |     |     ')
            print(f'  {s4}  |  {s5}  |  {s6}  ')
            print(f'     |     |     ')
            print(f'-----+-----+-----')
            print(f'     |     |     ')
            print(f'  {s7}  |  {s8}  |  {s9}  ')
            print(f'     |     |     ')
            print('\n')
            print('Peça X ganhou!\n')
            i = 13 # Ao qualquer um ganhar, as jogadas param de ser contabilizadas e o loop do jogo acaba. (i > 12)
            x += 1
        elif s1 == 'O' and s2 == 'O' and s3 == 'O' or s4 == 'O' and s5 == 'O' and s6 == 'O' or s7 == 'O' and s8 == 'O' and s9 == 'O' or s1 == 'O' and s4 == 'O' and s7 == 'O' or s2 == 'O' and s5 == 'O' and s8 == 'O' or s3 == 'O' and s6 == 'O' and s9 == 'O' or s1 == 'O' and s5 == 'O' and s9 == 'O' or s3 == 'O' and s5 == 'O' and s7 == 'O':
            print(f'     |     |     ')
            print(f'  {s1}  |  {s2}  |  {s3}  ')
            print(f'     |     |     ')
            print(f'-----+-----+-----')
            print(f'     |     |     ')
            print(f'  {s4}  |  {s5}  |  {s6}  ')
            print(f'     |     |     ')
            print(f'-----+-----+-----')
            print(f'     |     |     ')
            print(f'  {s7}  |  {s8}  |  {s9}  ')
            print(f'     |     |     ')
            print('\n')
            print('Peça O ganhou!')
            i = 13
            o += 1
        elif i == 12:
            print('Velha!')
            v += 1
    else:
        resp = input('Deseja jogar novamente? s/n:')
        system('clear')
else: # Fim de jogo, hora de contar as vitórias e empates!
    print('Jogo finalizado!')
    print(f'X ganhou {x} vez(es)')
    print(f'O ganhou {o} vez(es)')
    print(f'Deu velha {v} vez(es)')
