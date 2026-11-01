# Jogo da Velha - Trabalho 2ª Avaliação (Coding)

# Matriz do tabuleiro: tabuleiro[i][j] -> i = linha, j = coluna
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Tabuleiro com os números das linhas e colunas visíveis
print("    1   2   3")
for i in range(3):                      # percorre cada linha
    linhaTexto = str(i + 1) + "  "
    for j in range(3):                  # percorre cada coluna da linha
        linhaTexto = linhaTexto + " " + tabuleiro[i][j] + " "
        if j < 2:
            linhaTexto = linhaTexto + "|"
    print(linhaTexto)
    if i < 2:
        print("   ---+---+---")


        # Placar acumulado entre as partidas
    vitoriasX = 0
    vitoriasO = 0
    empates = 0


# MENU PRINCIPAL (Dia 2)
rodando = True                      # booleano: o programa roda enquanto for True
while rodando:
    print("")
    print("===== JOGO DA VELHA =====")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    # Validação da opção: repete até digitar um número de 1 a 4
    opcao = 0
    opcaoValida = False
    while opcaoValida == False:
        entrada = input("Escolha uma opção (1 a 4): ")
        for n in range(1, 5):               # opções válidas: "1" a "4"
            if entrada == str(n):
                opcaoValida = True
                opcao = n
        if opcaoValida == False:
            print("Entrada inválida! Digite um número de 1 a 4.")

    if opcao == 4:
        print("Obrigado por jogar!")
        rodando = False

# Redireciona o jogador conforme a opção escolhida
    if opcao == 1:
        print("")
        print("--- PARTIDA ---")
        # Exibe o tabuleiro com os números das linhas e colunas visíveis
        print("    1   2   3")
        for i in range(3):                      # percorre cada linha
            linhaTexto = str(i + 1) + "  "
            for j in range(3):                  # percorre cada coluna da linha
                linhaTexto = linhaTexto + " " + tabuleiro[i][j] + " "
                if j < 2:
                    linhaTexto = linhaTexto + "|"
            print(linhaTexto)
            if i < 2:
                print("   ---+---+---")
        print("(As jogadas serão implementadas nos próximos commits)")   #REALIZAR A ALTERAÇÃO POSTERIORMENTE AO DAR MERGE NOS CÓDIGOS
    elif opcao == 2:
        print("")
        print("=== REGRAS ===")
        print("- Dois jogadores se alternam marcando X ou O em uma casa vazia.")
        print("- Informe a linha e a coluna (de 1 a 3) da casa desejada.")
        print("- Vence quem completar uma linha, coluna ou diagonal.")
        print("- Se o tabuleiro encher sem vencedor, é empate.")
    elif opcao == 3:
        print("")
        print("=== PLACAR ===")
        print("Vitórias de X: " + str(vitoriasX))
        print("Vitórias de O: " + str(vitoriasO))
        print("Empates: " + str(empates))
    elif opcao == 4:
        print("Obrigado por jogar!")
        rodando = False



