import funcs
import time


def iniciarmines():
    saldo = 0

    print("-"*26)
    print(f"{'BEM VINDO AO MINES':^26}")
    print("-"*26,"\n")

    while True:
        try:
            saldo = float(input("Digite seu saldo: R$"))
            while saldo <= 0:
                saldo = float(input("INVÁLIDO! Digite um saldo maior que 0: R$"))
            break
        except ValueError:
            print("INVÁLIDO! Digite valores.\n")
    print()
            
    print("SALVANDOO...\n")
    time.sleep(0.8)

    while True:
        if saldo == 0:
            print("Saldo Zerado! Volte e Jogue Novamente.\n")
            time.sleep(1)
            break

        cont = 0
        matriz_real = funcs.cria_matriz()
        matriz_tela = funcs.cria_matriz()

        while True:
            try:
                valor_jogada = float(input("Valor da Jogada[>= R$1,00]: R$"))
                while valor_jogada > saldo or valor_jogada < 1:
                    valor_jogada = float(input("INVÁLIDO! Valor da Jogada[>= R$1]: R$"))
                break
            except ValueError:
                print("INVÁLIDO! Digite valores.\n")

        while True:
            try:
                num_bombas = int(input("Digite o número de bombas[1 a 20]: "))
                while num_bombas < 1 or num_bombas >= 21:
                    print("Número de bombas INVÁLIDO")
                    num_bombas = int(input("Digite novamente o número de bombas[1 a 20]: "))
                break
            except:
                print("INVÁLIDO! Digite valores inteiros.\n")
        print()

        funcs.bombas(matriz_real,num_bombas)

        input("APERTE 'ENTER' PARA INICIAR: \n")
        print("Preparando as bombas... \n")
        time.sleep(1)

        funcs.printa_matriz(matriz_tela)


        while True:
            while True:
                try:
                    num_linha = int(input("Linha: "))
                    while num_linha < 1 or num_linha > 5:
                        num_linha = int(input("INVÁLIDO! Linha: "))

                    num_coluna = int(input("Coluna: "))
                    while num_coluna < 1 or num_coluna > 5:
                        num_coluna = int(input("INVÁLIDO! Coluna: "))
                    break
                except ValueError:
                    print("INVÁLIDO! Digite valores inteiros.\n")
            print()
            print("Validandoo...\n")
            time.sleep(0.6)

            if funcs.valida_jogada(matriz_tela,num_linha-1,num_coluna-1) == False:
                print("JOGADA JÁ REALIZADA \n")
                time.sleep(0.5)
                funcs.printa_matriz(matriz_tela)
            
            elif funcs.atualiza_matriz(matriz_real,num_linha-1,num_coluna-1) == True:
                funcs.atualiza_matriz(matriz_tela,num_linha-1,num_coluna-1)
                cont += 1
                retorno = funcs.retorno(num_bombas,cont,valor_jogada)

                if cont == (25-num_bombas):
                    print("VOCÊ ACERTOU TODAS AS CASASS\U0001F631\U0001F631")
                    saldo += retorno
                    time.sleep(1)
                    break
                else:
                    print("PARABÉNS :)")
                    print(f"Retorno: +R${retorno:.2f}")

                continuar = input("Jogar mais uma vez [S/N]: ").lower()
                while continuar not in "sn" or continuar == '':
                    continuar = input("Jogar mais uma vez [S/N]: ").lower()

                print()

                if continuar == 'n':
                    print("Saindo...")
                    saldo += retorno
                    time.sleep(1)
                    break
                else:
                    funcs.printa_matriz(matriz_tela)
                
            else:
                print(".....BUMMM\U0001F4A5\U0001F4A5.....")
                time.sleep(0.5)
                print("NÃO FOI DESSA VEZ :(")
                saldo -= valor_jogada
                time.sleep(1)
                break

        print()
        print(f"SALDO FINAL: R${saldo:.2f}\n")
        time.sleep(1)
        print("GABARITO: ")
        time.sleep(0.5)
        funcs.printa_matriz(matriz_real)
        print()
        resp = input("Jogar mais uma vez [S/N]: ").lower()
        while resp not in "sn" or resp == '':
            resp = input("Jogar mais uma vez [S/N]: ").lower()
        
        print()

        if resp == 'n':
            break

    print("OBRIGADO POR JOGAR!")
    print(f"SALDO FINAL: R${saldo:.2f}\n")
    input('Aperte "ENTER" para voltar')