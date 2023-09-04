from random import randint


def atualiza_matriz(matriz,num_linha,num_coluna):
    
    if matriz[num_linha][num_coluna] == "\U0001F4A3":
        return False
    else:
        matriz[num_linha][num_coluna] = "  "
        return True

def valida_jogada(matriz,num_linha,num_coluna):
    if matriz[num_linha][num_coluna] != "\u2B50":
        return False
    else:
        return True
    
def cria_matriz():
    matriz_base = []
    for l in range(5):
        coluna = []
        for c in range(5):
            coluna.append("\u2B50")
        matriz_base.append(coluna)
    
    return matriz_base

def printa_matriz(matriz):
    for z in range(5):
        if z == 0:
            print(f'{ z+1:>7}',end=" ")
        elif z == 1:
            print(f'{z+1:>4}',end="")
        else:
            print(f'{z+1:>5}',end="")
    print()
    for l in range(5):
        print("  ","-"*26)
        for c in range(5):
            if c == 0:
                print(f"{l+1}  | {matriz[l][c]}", end=" ")
            elif c == 4:
                print(f"| {matriz[l][c]} |")
            else:
                print(f"| {matriz[l][c]}", end=' ')
        if l == 4:
            print("  ","-"*26)

def retorno(num_bombas,num_jogadas,valor_jogado):
    valor = (num_bombas * 0.05) + (num_jogadas*0.05)
    return valor_jogado * valor

def bombas(matriz,num_bombas):
    for i in range(num_bombas):
        num_linha = randint(0,4)
        num_coluna = randint(0,4)

        while matriz[num_linha][num_coluna] == "\U0001F4A3":
            num_linha = randint(0,4)
            num_coluna = randint(0,4)

        matriz[num_linha][num_coluna] = "\U0001F4A3"

    return matriz