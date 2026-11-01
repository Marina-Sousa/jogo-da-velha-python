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




