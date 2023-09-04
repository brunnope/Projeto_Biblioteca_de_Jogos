from jogodavelha import iniciarjogodavelha
from mines import iniciarmines
import os
from time import sleep

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

menu = True

while menu is True:
    limpar_console()
    print("-"*26)
    print(f"{'BIBLIOTECA DE JOGOS':^26}")
    print("-"*26)
    print(f"{'Qual jogo deseja jogar?':^26}\n")

    print("1 - Mines")
    print("2 - Jogo da velha")
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
        print("- Iniciando Mines... \n")
        sleep(1)
        limpar_console()
        iniciarmines()

    elif escolha == 2:
        print("- Iniciando jogo da velha... \n")
        sleep(1)
        limpar_console()
        iniciarjogodavelha()

    elif escolha == 3:
        print("Saindo...\n")
        sleep(1)
        menu = False

print("VOLTE SEMPRE :)")