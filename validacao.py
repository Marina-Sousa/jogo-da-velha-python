# === DIA 4 - COMMIT 5: Alternância de turnos entre jogadores ===
# Tabuleiro de Matriz para testes
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

simbolo_atual = "X"
jogo_ativo = True
jogadas_realizadas = 0

# Simulação de turnos
while jogo_ativo == True and jogadas_realizadas < 9:
    print("\n--- É a vez do jogador:", simbolo_atual, "---")
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
    # Grava jogada na matriz            
    tabuleiro[linha][coluna] = simbolo_atual
    jogadas_realizadas += 1
    print("Jogada feita na linha", linha + 1, "e coluna", coluna + 1)

    # 4. Alternância de turno
    if simbolo_atual == "X":
        simbolo_atual = "O"
    else:
        simbolo_atual = "X"

print("Partida finalizada!")