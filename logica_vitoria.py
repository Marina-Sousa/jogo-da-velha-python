# Módulo de Verificação de Vitória - Jogo da Velha (correção de requisitos permitidos)
# Integrante: Sílvia

# Estrutura inicial do tabuleiro de teste
tabuleiro_exemplo = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Variável para testar o jogador atual
jogador_atual = "X"
vitoria = False

# Verificação de linhas e colunas usando laços for
for i in range(3):
    if tabuleiro_exemplo[i][0] == jogador_atual and tabuleiro_exemplo[i][1] == jogador_atual and tabuleiro_exemplo[i][2] == jogador_atual:
        vitoria = True
    if tabuleiro_exemplo[0][i] == jogador_atual and tabuleiro_exemplo[1][i] == jogador_atual and tabuleiro_exemplo[2][i] == jogador_atual:
        vitoria = True

# Verificação das diagonais
if tabuleiro_exemplo[0][0] == jogador_atual and tabuleiro_exemplo[1][1] == jogador_atual and tabuleiro_exemplo[2][2] == jogador_atual:
    vitoria = True
if tabuleiro_exemplo[0][2] == jogador_atual and tabuleiro_exemplo[1][1] == jogador_atual and tabuleiro_exemplo[2][0] == jogador_atual:
    vitoria = True

if vitoria:
    print("Vitória detectada!")
else:
    print("Nenhuma vitória ainda.")

    # Verificação de empate (conta quantas casas ainda estão vazias)
vazias = 0
for i in range(3):
    for j in range(3):
        if tabuleiro_exemplo[i][j] == " ":
            vazias = vazias + 1

if vazias == 0 and vitoria == False:
    print("Deu empate!")

    # Placar acumulado entre as partidas
vitorias_jogador_x = 0
vitorias_jogador_o = 0
total_empates = 0

# Exemplo de atualização após o término de uma partida
# (Você pode incrementar essas variáveis quando houver vitória ou empate)
vitorias_jogador_x = vitorias_jogador_x + 1

print("Placar Final:")
print("Jogador X:", vitorias_jogador_x)
print("Jogador O:", vitorias_jogador_o)
print("Empates:", total_empates)

# Estatísticas da sessão (total de partidas, vitórias, empates e porcentagens)
total_partidas = vitorias_jogador_x + vitorias_jogador_o + total_empates

if total_partidas > 0:
    porcentagem_x = (vitorias_jogador_x / total_partidas) * 100
    porcentagem_o = (vitorias_jogador_o / total_partidas) * 100
    porcentagem_empates = (total_empates / total_partidas) * 100
else:
    porcentagem_x = 0.0
    porcentagem_o = 0.0
    porcentagem_empates = 0.0

print("--- Estatisticas da Sessao ---")
print("Total de partidas:", total_partidas)
print("Vitorias do Jogador X:", vitorias_jogador_x, "-", porcentagem_x, "%")
print("Vitorias do Jogador O:", vitorias_jogador_o, "-", porcentagem_o, "%")
print("Empates:", total_empates, "-", porcentagem_empates, "%")