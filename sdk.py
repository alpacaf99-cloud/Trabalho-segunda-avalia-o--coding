total_partidas = 0
opcao_menu = 0

while opcao_menu != 4:
    print("\n=====================================")
    print("        SUDOKU 4x4    ")
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
            print("1 - Nivel Facil   (8 numeros fixos)")
            print("2 - Nivel Medio   (6 numeros fixos)")
            print("3 - Nivel Dificil (4 numeros fixos)")
            print("4 - Voltar ao menu principal")

            valida_dif = False
            while valida_dif == False:
                dif_str = input("Escolha o nivel (1 a 4): ")
                for n in range(1, 5):
                    if dif_str == str(n):
                        valida_dif = True
                        opcao_dificuldade = n
                if valida_dif == False:
                    print("[ENTRADA INVALIDA] Digite apenas um numero de 1 a 4.")

            if opcao_dificuldade >= 1 and opcao_dificuldade <= 3:
                total_partidas = total_partidas + 1
                print("Dificuldade selecionada para a partida solo:", opcao_dificuldade)

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
        print("\nESTATISTICAS DA SESSAO")
        print("Partidas iniciadas:", total_partidas)
        voltar = "0"
        while voltar != "1":
            voltar = input("Digite 1 para voltar ao menu principal: ")
            if voltar != "1":
                print("Opcao invalida. Digite 1 para voltar.")

    elif opcao_menu == 4:
        print("Programa encerrado.")