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