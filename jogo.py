total_partidas = 0
vitoria_player1 = 0
vitoria_player2 = 0
empates = 0
opcao_menu = 0

while opcao_menu != 4:
    print("\n ===========================")
    print("         SUDOKU COMPETITIVO (4X4) - MENU          ")
    print("=====================================")
    print("\n")
    print(" 1 - jogar (Escolher Dificuldade)" ) 
    print(" 2 - sobre o jogo e regras" )
    print(" 3 - estatisticas de vitorias " )
    print(" 4 - fechar o programa" )
    print("=================================")

validar_menu = false
opcao_string = input("Escolha uma opcao (de 1 a 4): ")
for n in range(1,5):
    if opcao_string == str(n):
        validar_menu = true
        opcao_menu = n
if validar_menu == false:
    print("\n ENTRADA INVALIDA digite apenas numeros entre 1 a 5") 
