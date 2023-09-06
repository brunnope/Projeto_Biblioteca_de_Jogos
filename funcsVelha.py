marcador = ['X', 'O']
from random import randint
from time import sleep

def iniciarjogodavelhacomputador():
    empate = 0
    win_x = 0
    win_o = 0
    
    print("-"*26)
    print(f"{'CONTRA A MAQUINA':^26}")
    print("-"*26)

    while True:
        turn = 0
        board = criarvelha()
        ganhador = vencedor(board, turn)
        jogador = 0
        while not ganhador:
            display(board, turn)
            print('Turno de', marcador[jogador])
            if jogador == 0:
                linha = validarinput('Digite a Linha: ')
                coluna = validarinput('Digite a Coluna: ')
            else:
                print("\nMáquina escolhendo...")
                sleep(1)
                print(linha,coluna)
                linha,coluna = jogadaMaquina(board,turn,linha,coluna)
                print(linha,coluna)

            if validarmovimento(board, linha, coluna):
                movimento(board, linha, coluna, jogador)
                jogador = (jogador+1) % 2
                turn += 1
            
            else:
                print('Posição já ocupada por', board[linha][coluna])
            ganhador = vencedor(board, turn)
        print('*' * 20)
        display(board, turn)
        if ganhador == 'velha':
            print(f"Deu {ganhador}!")
        else:
            print(f'O Ganhador foi: {ganhador}!\n')
        
        empate, win_x, win_o = score(ganhador,empate,win_x,win_o)

        print(f"Vitórias jogador X: {win_x}")
        print(f"Vitórias jogador O: {win_o}")
        print(f"Empates: {empate} \n")

        resp = input("Jogar mais uma vez [S/N]: ").lower()
        while resp not in "sn" or resp == '':
            resp = input("Jogar mais uma vez [S/N]: ").lower()
        
        print()

        if resp == 'n':
            print("OBRIGADO POR JOGAR!\n")
            input('Aperte "ENTER" para voltar')
            break


def jogadaMaquina(board,turno,linha,coluna):
    errado_testes = False
    if turno > 2:
        if linha == 0 and coluna == 0:
            if board[0][1] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            elif board[1][0] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0
            elif board[1][1] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            
            #possiblidade de não ser sequencia
            elif board[2][0] == "X" and board[1][0] == ' ':
                linha = 1
                coluna = 0
            elif board[0][2] == "X" and board[0][1] == ' ':
                linha = 0
                coluna = 1
            elif board[2][2] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True
               
        elif linha == 0 and coluna == 1:
            if board[0][0] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            elif board[0][2] == "X" and board[0][1] == ' ':
                linha = 0
                coluna = 1
            elif board[1][1] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 1

            #possiblidade de não ser sequencia
            elif board[2][1] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True

        elif  linha == 0 and coluna == 2:
            if board[0][1] == "X" and board[0][0] == ' ':
                linha = 0
                coluna = 0
            elif board[1][2] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            elif board[1][1] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0
            
            #possiblidade de não ser sequencia
            elif board[0][0] == "X" and board[0][1] == ' ':
                linha = 0
                coluna = 1
            elif board[2][2] == "X" and board[1][2] == ' ':
                linha = 1
                coluna = 2
            elif board[2][0] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True
            
        elif linha == 1 and coluna == 0:
            if board[0][0] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0
            elif board[2][0] == "X" and board[0][0] == ' ':
                linha = 0
                coluna = 0
            elif board[1][1] == "X" and board[1][2] == ' ':
                linha = 1
                coluna = 2

            #possiblidade de não ser sequencia
            elif board[1][2] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True  

        elif linha == 1 and coluna == 1:
            if board[0][0] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            elif board[2][2] == "X" and board[0][0] == ' ':
                linha = 0
                coluna = 0

            elif board[2][0] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            elif board[0][2] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0

            elif board[1][0] == "X" and board[1][2] == ' ':
                linha = 1
                coluna = 2
            elif board[1][2] == "X" and board[1][0] == ' ':
                linha = 1
                coluna = 0

            elif board[0][1] == "X" and board[2][1] == ' ':
                linha = 2
                coluna = 1
            elif board[2][1] == "X" and board[0][1] == ' ':
                linha = 0
                coluna = 1
            else:
                errado_testes = True

        elif linha == 1 and coluna == 2:
            if board[0][2] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            elif board[2][2] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            elif board[1][1] == "X" and board[1][0] == ' ':
                linha = 1
                coluna = 0
            
            #possiblidade de não ser sequencia
            elif board[1][0] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True

        elif linha == 2 and coluna == 0:
            if board[1][0] == "X" and board[0][0] == ' ':
                linha = 0
                coluna = 0
            elif board[2][1] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            elif board[1][1] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            
            #possiblidade de não ser sequencia
            elif board[0][0] == "X" and board[1][0] == ' ':
                linha = 1
                coluna = 0
            elif board[2][2] == "X" and board[2][1] == ' ':
                linha = 2
                coluna = 1
            elif board[0][2] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True
        
        elif linha == 2 and coluna == 1:
            if board[2][0] == "X" and board[2][2] == ' ':
                linha = 2
                coluna = 2
            elif board[2][2] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0
            elif board[1][1] == "X" and board[0][1] == ' ':
                linha = 0
                coluna = 1

            #possiblidade de não ser sequencia
            elif board[0][1] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True
        
        elif linha == 2 and coluna == 2:
            if board[2][1] == "X" and board[2][0] == ' ':
                linha = 2
                coluna = 0
            elif board[1][2] == "X" and board[0][2] == ' ':
                linha = 0
                coluna = 2
            elif board[1][1] == "X" and board[0][0] == ' ':
                linha = 0
                coluna = 0
            
            #possiblidade de não ser sequencia
            elif board[2][0] == "X" and board[2][1] == ' ':
                linha = 2
                coluna = 1
            elif board[0][2] == "X" and board[1][2] == ' ':
                linha = 1
                coluna = 2
            elif board[0][0] == "X" and board[1][1] == ' ':
                linha = 1
                coluna = 1
            else:
                errado_testes = True

    if turno <= 2 or errado_testes:
        linha = randint(0,2)
        coluna = randint(0,2)
        while (board[linha][coluna] != ' '):
            linha = randint(0,2)
            coluna = randint(0,2)

    return linha,coluna


def iniciarjogodavelha2():
    empate = 0
    win_x = 0
    win_o = 0
    
    print("-"*26)
    print(f"{'2 JOGADORES':^26}")
    print("-"*26)

    while True:
        turn = 0
        board = criarvelha()
        ganhador = vencedor(board, turn)
        jogador = 0
        while not ganhador:
            display(board, turn)
            print('Turno de', marcador[jogador])
            if jogador == 0:
                linha = validarinput('Digite a Linha: ')
                coluna = validarinput('Digite a Coluna: ')
            else:
                linha = validarinput('Digite a Linha: ')
                coluna = validarinput('Digite a Coluna: ')

            if validarmovimento(board, linha, coluna):
                movimento(board, linha, coluna, jogador)
                jogador = (jogador+1) % 2
                turn += 1
            
            else:
                print('Posição já ocupada por', board[linha][coluna])
            ganhador = vencedor(board, turn)
        print('*' * 20)
        display(board, turn)
        if ganhador == 'velha':
            print(f"Deu {ganhador}!")
        else:
            print(f'O Ganhador foi: {ganhador}!\n')
        
        empate, win_x, win_o = score(ganhador,empate,win_x,win_o)

        print(f"Vitórias jogador X: {win_x}")
        print(f"Vitórias jogador O: {win_o}")
        print(f"Empates: {empate} \n")

        resp = input("Jogar mais uma vez [S/N]: ").lower()
        while resp not in "sn" or resp == '':
            resp = input("Jogar mais uma vez [S/N]: ").lower()
        
        print()

        if resp == 'n':
            print("OBRIGADO POR JOGAR!\n")
            input('Aperte "ENTER" para voltar')
            break

def criarvelha():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board


def display(board, turn):
    print()
    print('   1  2  3')
    for i in range(3):
        print(i+1, ' | '.join(board[i]))
        if i < 2:
            print('  ---------')
    print()
    print("Jogadas:", turn)


def validarinput(frase):
    try:
        n = int(input(frase))
        if n < 1 or n > 3:
            print('A linha e Coluna deve estar entre 1 e 3')
            return validarinput(frase)
        else:
            return n - 1
    except ValueError:
        print('Apenas Números')
        return validarinput(frase)


def validarmovimento(board, linha, coluna):
    if board[linha][coluna] == ' ':
        return True
    else:
        return False


def movimento(board, linha, coluna, player):
    board[linha][coluna] = marcador[player]


def vencedor(board, turn):
    if turn < 5:
        return False
    if turn >= 5:
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
                return board[i][0]

        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
                return board[0][i]

        if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]

        if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return False

        return "velha"

def score(ganhador,empate,win_x,win_o):

    if ganhador == "velha":
        empate += 1
    elif ganhador == "X":
        win_x += 1
    elif ganhador == "O":
        win_o += 1
    
    return empate,win_x,win_o
