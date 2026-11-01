# Exemplo de matriz com algumas posições já ocupadas para testes
tabuleiro = [
    ["X", " ", " "],
    [" ", "O", " "],
    [" ", " ", " "]
]
simbolo_atual = "X"

# === DIA 3 - COMMIT 4: Verificação de casa ocupada ===
casa_valida = False
while casa_valida == False:
    # Validação da Linha
    linha_valida = False
    while linha_valida == False:
        entrada_linha = input("Digite a linha (1, 2 ou 3): ")
        for n in range(1, 4):  # Passa por 1, 2 e 3
            if entrada_linha == str(n):
                linha_valida = True
                linha = n - 1  # Converte para índice da matriz (0, 1 ou 2)
        if linha_valida == False:
            print("Fora do limite do tabuleiro! Digite um número válido entre 1 e 3.")

    # Validação da Coluna
    coluna_valida = False
    while coluna_valida == False:
        entrada_coluna = input("Digite a coluna (1, 2 ou 3): ")
        for n in range(1, 4):  # Passa por 1, 2 e 3
            if entrada_coluna == str(n):
                coluna_valida = True
                coluna = n - 1  # Converte para índice da matriz (0, 1 ou 2)
        if coluna_valida == False:
            print("Fora do limite do tabuleiro! Digite um número válido entre 1 e 3.")
    # 3. Verificação de casa ocupada na matriz
        if tabuleiro[linha][coluna] != " ":
            print("Esta casa já está ocupada por '" + tabuleiro[linha][coluna] + "'! Escolha outra posição.")
        else:
            casa_valida = True
print("Jogada feita na linha", linha + 1, "e coluna", coluna + 1)