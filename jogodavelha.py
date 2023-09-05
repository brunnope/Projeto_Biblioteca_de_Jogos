import funcsVelha
import os
from time import sleep

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")


funcsVelha.iniciarjogodavelhacomputador()
def IniciaJogoDaVelha():
    while True:
        limpar_console()
        print("-"*26)
        print(f"{'BEM VINDO AO JOGO DA VELHA':^26}")
        print("-"*26)

        print("1 - Jogar com Computador")
        print("2 - Jogar com 2 jogadores")
        print("3 - Sair")
        print("-"*26)
        
        while True:
            try:
                escolha = int(input("Escolha: "))
                while escolha < 1 or escolha > 3:
                    escolha = int(input("INVÁLIDO! Digite entre 1 e 3: "))
                break
            except ValueError:
                print("INVÁLIDO! Digite valores.\n")
                sleep(1)

        print()

        if escolha == 1:
            print("- Iniciando contra o computador... \n")
            sleep(1)
            limpar_console()
            funcsVelha.iniciarjogodavelhacomputador()
            

        elif escolha == 2:
            print("- Iniciando de 2 jogadores... \n")
            sleep(1)
            limpar_console()
            funcsVelha.iniciarjogodavelha2()

        elif escolha == 3:
            print("Saindo...\n")
            sleep(1)
            break

print("VOLTE SEMPRE :)")