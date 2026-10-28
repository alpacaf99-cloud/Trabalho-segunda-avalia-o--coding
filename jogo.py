rodando = True

while rodando == True:
    print("")
    print("=========================")
    print("          JOGOS NO TERMINAL")
    print("==================================")
    print("1 - Jogo da Velha")
    print("2 - Sudoku")
    print("3 - Ver regras")
    print("4 - Sair")
    print("========================================")

    opcao = 0
    valida = False
    while valida == False:
        entrada = input("Escolha uma opção (1 a 4): ")
        for n in range(1, 6):
            if entrada == str(n):
                valida = True
                opcao = n
        if valida == False:
            print("Entrada inválida! Digite um número de 1 a 5.")

    # Tratamento da opção escolhida
    if opcao == 1:
        print("Você escolheu: Jogo da Velha")
    elif opcao == 2:
        print("Você escolheu: Sudoku")
    elif opcao == 3:
        print("Você escolheu: Ver regras")
    else:
        print("Encerrando o programa. Até a próxima!")
        rodando = False
