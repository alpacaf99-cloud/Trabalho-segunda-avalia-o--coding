total_partidas = 0
vitorias = 0
pontuacao_total_sessao = 0
opcao_menu = 0

while opcao_menu != 4:
    print("\n=====================================")
    print("         SUDOKU 4x4    ")
    print("=====================================")
    print("1 - Jogar (Escolher Dificuldade)")
    print("2 - Sobre o jogo e regras")
    print("3 - Estatisticas da sessao")
    print("4 - Fechar o programa")
    print("-------------------------------------")

    valida_menu = False
    while valida_menu == False:
        opcao_str = input("Escolha uma opcao (1 a 4): ")
        for n in range(1, 5):
            if opcao_str == str(n):
                valida_menu = True
                opcao_menu = n
        if valida_menu == False:
            print("[ENTRADA INVALIDA] Digite apenas um numero de 1 a 4.")
    if opcao_menu == 1:
        opcao_dificuldade = 0
        while opcao_dificuldade != 4:
            print("\nSELECIONE A DIFICULDADE")
            print("1 - Nivel Facil   (8 numeros)")
            print("2 - Nivel Medio   (6 numeros)")
            print("3 - Nivel Dificil (4 numeros)")
            print("4 - Voltar ao menu principal")
            valida_dif = False
            while valida_dif == False:
                dif_str = input("Escolha o nivel (1 a 4): ")
                for n in range(1, 5):
                    if dif_str == str(n):
                        valida_dif = True
                        opcao_dificuldade = n
                if valida_dif == False:
                    print("ENTRADA INVALIDA Digite apenas um numero de 1 a 4.")
            if opcao_dificuldade >= 1 and opcao_dificuldade <= 3:
                total_partidas = total_partidas + 1
                gabarito = [
                    [1, 2, 3, 4],
                    [3, 4, 1, 2],
                    [2, 1, 4, 3],
                    [4, 3, 2, 1],
                ]
                tabuleiro = [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                ]
                fixo = [
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                    [False, False, False, False],
                ]

                if opcao_dificuldade == 1:
                    posicoes_i = [0, 0, 1, 1, 2, 2, 3, 3]
                    posicoes_j = [0, 3, 1, 2, 0, 3, 1, 2]
                elif opcao_dificuldade == 2:
                    posicoes_i = [0, 0, 1, 2, 3, 3]
                    posicoes_j = [0, 2, 1, 3, 0, 2]
                else:
                    posicoes_i = [0, 1, 2, 3]
                    posicoes_j = [0, 3, 0, 3]

                for idx in range(len(posicoes_i)):
                    li = posicoes_i[idx]
                    co = posicoes_j[idx]
                    tabuleiro[li][co] = gabarito[li][co]
                    fixo[li][co] = True
             pontos_partida = 0
                partida_ativa = True
                while partida_ativa == True:
                    print("\n      1   2     3   4")
                    print("    +-------+-------+")
                    for i in range(4):
                        linha_fmt = str(i + 1) + "   | "
                        for j in range(4):
                            val_str = "."
                            if tabuleiro[i][j] != 0:
                                val_str = str(tabuleiro[i][j])
                            linha_fmt = linha_fmt + val_str + " "
                            if j == 1:
                                linha_fmt = linha_fmt + "| "
                        linha_fmt = linha_fmt + "|"
                        print(linha_fmt)
                        if i == 1 or i == 3:
                            print("    +-------+-------+")
                    print("Pontuação atual:", pontos_partida)
