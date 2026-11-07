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
                    # Menu de ações da partida
                    print("\nMenu da Partida:")
                    print("1 - Inserir/Alterar número")
                    print("2 - Desistir e voltar")
                    valida_acao = False
                    acao = 0
                    while valida_acao == False:
                        ent_acao = input("Escolha uma opção (1 ou 2): ")
                        if ent_acao == "1" or ent_acao == "2":
                            valida_acao = True
                            acao = int(ent_acao)
                        else:
                            print("[ENTRADA INVALIDA] Digite 1 ou 2.")
                    if acao == 2:
                        print("Você desistiu da partida.")
                        partida_ativa = False
                    else:
                        valida_l = False
                        linha = -1
                        while valida_l == False:
                            ent_l = input("Digite a LINHA (1 a 4): ")
                            for n in range(1, 5):
                                if ent_l == str(n):
                                    valida_l = True
                                    linha = n - 1
                            if valida_l == False:
                                print("[ENTRADA INVALIDA] Digite um número de 1 a 4.")
                        valida_c = False
                        coluna = -1
                        while valida_c == False:
                            ent_c = input("Digite a COLUNA (1 a 4): ")
                            for n in range(1, 5):
                                if ent_c == str(n):
                                    valida_c = True
                                    coluna = n - 1
                            if valida_c == False:
                                print("[ENTRADA INVALIDA] Digite um número de 1 a 4.")
                        if fixo[linha][coluna] == True:
                            print("\n[JOGADA INVALIDA] Esta casa contém um número fixo inicial e não pode ser alterada!")
                        else:
                            valida_v = False
                            valor = -1
                            while valida_v == False:
                                ent_v = input("Digite o valor para a casa (1 a 4): ")
                                for n in range(1, 5):
                                    if ent_v == str(n):
                                        valida_v = True
                                        valor = n
                                if valida_v == False:
                                    print("[ENTRADA INVALIDA] Digite um número de 1 a 4.")
                            conflito = False
                            # 1. Verifica repetido na mesma linha
                            for j in range(4):
                                if j != coluna and tabuleiro[linha][j] == valor:
                                    conflito = True
                            # 2. Verifica repetido na mesma coluna
                            for i in range(4):
                                if i != linha and tabuleiro[i][coluna] == valor:
                                    conflito = True
                            # 3. Verifica repetido no mesmo bloco 2x2.
                            inicio_i = (linha // 2) * 2
                            inicio_j = (coluna // 2) * 2
                            for i in range(inicio_i, inicio_i + 2):
                                for j in range(inicio_j, inicio_j + 2):
                                    if (i != linha or j != coluna) and tabuleiro[i][j] == valor:
                                        conflito = True
                            if conflito == True:
                                print("\n[JOGADA INVALIDA] O número", valor, "viola as regras do Sudoku (já existe na linha, coluna ou bloco 2x2)!")
                            else:
                                tabuleiro[linha][coluna] = valor
                                pontos_partida = pontos_partida + 10
                                print("\n-> Jogada realizada com sucesso! (+10 pontos)")
                                vazias = 0
                                for i in range(4):
                                    for j in range(4):
                                        if tabuleiro[i][j] == 0:
                                            vazias = vazias + 1
                                if vazias == 0:
                                    print("\n      1   2     3   4")
                                    print("    +-------+-------+")
                                    for i in range(4):
                                        linha_fmt = str(i + 1) + "   | "
                                        for j in range(4):
                                            linha_fmt = linha_fmt + str(tabuleiro[i][j]) + " "
                                            if j == 1:
                                                linha_fmt = linha_fmt + "| "
                                        linha_fmt = linha_fmt + "|"
                                        print(linha_fmt)
                                        if i == 1 or i == 3:
                                            print("    +-------+-------+")
                                    print("\n=========================================")
                                    print(" PARABÉNS! VOCÊ COMPLETOU O SUDOKU 4x4! ")
                                    print(" Pontuação Final da Partida:", pontos_partida)
                                    print("=========================================")
                                    vitorias = vitorias + 1
                                    pontuacao_total_sessao = pontuacao_total_sessao + pontos_partida
                                    partida_ativa = False
                                    opcao_dificuldade = 4
    elif opcao_menu == 2:
        print("\nREGRAS DO SUDOKU 4x4")
        print("1. O jogo tem um jogador.")
        print("2. Cada casa aceita um numero de 1 a 4.")
        print("3. Nao repita numero na mesma linha.")
        print("4. Nao repita numero na mesma coluna.")
        print("5. Nao repita numero no mesmo bloco 2x2.")
        print("6. Cada jogada valida soma 10 pontos.")
        print("7. Complete o tabuleiro para concluir a partida.")
        voltar = "0"
        while voltar != "1":
            voltar = input("Digite 1 para voltar ao menu principal: ")
            if voltar != "1":
                print("Opcao invalida. Digite 1 para voltar.")
        elif opcao_menu == 3:
        print("\n=====================================")
        print("       ESTATISTICAS DA SESSAO        ")
        print("=====================================")
        print("Partidas iniciadas:", total_partidas)
        print("Partidas concluídas (Vitórias):", vitorias)
        print("Pontuação acumulada total:", pontuacao_total_sessao)

        if total_partidas > 0:
            taxa_vitoria = (vitorias / total_partidas) * 100.0
            print("Taxa de conclusão:", float(int(taxa_vitoria * 100)) / 100, "%")
            media_pontos = pontuacao_total_sessao / total_partidas
            print("Média de pontos por partida:", float(int(media_pontos * 100)) / 100)
        else:
            print("Nenhuma partida jogada nesta sessão.")
        print("-------------------------------------")

        voltar = "0"
        while voltar != "1":
            voltar = input("Digite 1 para voltar ao menu principal: ")
            if voltar != "1":
                print("Opcao invalida. Digite 1 para voltar.")
