# Marina Sousa - Leitura, Validação de Entradas e Turnos
casa_valida = False
while casa_valida == False:
    # 1. Validação da Linha
    linha_valida = False
    while linha_valida == False: # Repete até que entrada_linha == str(n)
        entrada_linha = input("Digite a linha (1, 2 ou 3): ")
        for n in range(1, 4):  # Passa por 1, 2 e 3
            if entrada_linha == str(n):
                linha_valida = True
                linha = n - 1  # Converte para índice da matriz (0, 1 ou 2)
            if linha_valida == False:
                print("Fora do limite do tabuleiro! Digite um número válido entre 1 e 3.")

    # 2. Validação da Coluna
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

    # Grava jogada na matriz            
    tabuleiro[linha][coluna] = simbolo_atual

    # 4. Alternância de turno
    if simbolo_atual == "X":
        simbolo_atual = "O"
    else:
        simbolo_atual = "X"