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
