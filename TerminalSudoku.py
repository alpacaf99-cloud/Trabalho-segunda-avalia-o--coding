#menu de ações da partida
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