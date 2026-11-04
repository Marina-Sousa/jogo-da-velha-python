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
        print("")
        print("=== ESTATÍSTICAS DA SESSÃO ===")
        total_partidas = vitoriasX + vitoriasO + empates
        
        if total_partidas > 0:
            porcentagem_x = (vitoriasX / total_partidas) * 100
            porcentagem_o = (vitoriasO / total_partidas) * 100
            porcentagem_empates = (empates / total_partidas) * 100
        else:
            porcentagem_x = 0.0
            porcentagem_o = 0.0
            porcentagem_empates = 0.0
            
        print("Total de partidas:", total_partidas)
        print("Vitórias do Jogador X:", vitoriasX, "-", porcentagem_x, "%")
        print("Vitórias do Jogador O:", vitoriasO, "-", porcentagem_o, "%")
        print("Empates:", empates, "-", porcentagem_empates, "%")
        
        print("\nObrigado por jogar!")
        rodando = False

#DIA 3 

    if opcao == 1:
        jogarNovamente = True
        while jogarNovamente:
            # Reinício da partida: limpa a matriz com for aninhado
            for i in range(3):                  # percorre as linhas
                for j in range(3):              # percorre as colunas de cada linha
                    tabuleiro[i][j] = " "
            print("[TESTE] matriz depois de limpar:", tabuleiro)   # remover depois!!!!!

            print("")
            print("--- PARTIDA ---")
            # (aqui continua o bloco de exibição do tabuleiro, igual ao anterior,
            #  só com mais um nível de recuo)

            # Lógica de turnos e jogadas (adaptada do validacao.py)
            simbolo_atual = "X"
            jogo_ativo = True
            jogadas_realizadas = 0

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
                    
                    # Verificação de casa ocupada na matriz
                    if tabuleiro[linha][coluna] != " ":
                        print("Esta casa já está ocupada por '" + tabuleiro[linha][coluna] + "'! Escolha outra posição.")
                    else:
                        casa_valida = True

                # Grava jogada na matriz
                tabuleiro[linha][coluna] = simbolo_atual
                jogadas_realizadas += 1

                # Exibe o tabuleiro atualizado após a jogada
                print("    1   2   3")
                for i in range(3):
                    linhaTexto = str(i + 1) + "  "
                    for j in range(3):
                        linhaTexto = linhaTexto + " " + tabuleiro[i][j] + " "
                        if j < 2:
                            linhaTexto = linhaTexto + "|"
                    print(linhaTexto)
                    if i < 2:
                        print("   ---+---+---")

                # Verificação de Vitória (sua lógica adaptada para a matriz real do jogo)
                vitoria = False
                for i in range(3):
                    if tabuleiro[i][0] == simbolo_atual and tabuleiro[i][1] == simbolo_atual and tabuleiro[i][2] == simbolo_atual:
                        vitoria = True
                    if tabuleiro[0][i] == simbolo_atual and tabuleiro[1][i] == simbolo_atual and tabuleiro[2][i] == simbolo_atual:
                        vitoria = True

                if tabuleiro[0][0] == simbolo_atual and tabuleiro[1][1] == simbolo_atual and tabuleiro[2][2] == simbolo_atual:
                    vitoria = True
                if tabuleiro[0][2] == simbolo_atual and tabuleiro[1][1] == simbolo_atual and tabuleiro[2][0] == simbolo_atual:
                    vitoria = True

                if vitoria:
                    print("Jogador", simbolo_atual, "venceu a partida!")
                    if simbolo_atual == "X":
                        vitoriasX = vitoriasX + 1
                    else:
                        vitoriasO = vitoriasO + 1
                    jogo_ativo = False
                else:
                    # Verificação de Empate
                    vazias = 0
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == " ":
                                vazias = vazias + 1

                    if vazias == 0:
                        print("Deu empate!")
                        empates = empates + 1
                        jogo_ativo = False
                    else:
                        # Alternância de turno se o jogo continuar
                        if simbolo_atual == "X":
                            simbolo_atual = "O"
                        else:
                            simbolo_atual = "X"

            # Jogar novamente? (repete até responder s ou n)
            respostaValida = False
            while respostaValida == False:
                resposta = input("Jogar novamente? (s/n): ")
                if resposta == "s" or resposta == "S":
                    respostaValida = True
                    jogarNovamente = True
                elif resposta == "n" or resposta == "N":
                    respostaValida = True
                    jogarNovamente = False
                else:
                    print("Entrada inválida! Digite s ou n.")


