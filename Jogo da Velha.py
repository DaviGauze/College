tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogadores = ["X", "O"]
jogador_atual = 0
numero_jogo = 1  

while True:
    print("Jogo %d:" % numero_jogo)  

    for linha in tabuleiro:
        print("| %s | %s | %s |" % (linha[0], linha[1], linha[2]))
        print("-" * 13)

    linha, coluna = map(int, input("Jogador %s, insira sua jogada (linha e coluna, de 1 a 3): " % jogadores[jogador_atual]).split())
    linha -= 1
    coluna -= 1

    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada. Tente novamente.")
        continue

    tabuleiro[linha][coluna] = jogadores[jogador_atual]

    print("Estado atual do Jogo %d:" % numero_jogo)
    for linha in tabuleiro:
        print("| %s | %s | %s |" % (linha[0], linha[1], linha[2]))
        print("-" * 13)

    ganhou = False
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogadores[jogador_atual]:  
            ganhou = True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogadores[jogador_atual]: 
            ganhou = True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogadores[jogador_atual]: 
        ganhou = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogadores[jogador_atual]: 
        ganhou = True

    if ganhou:
        print("Estado final do Jogo %d:" % numero_jogo)
        for linha in tabuleiro:
            print("| %s | %s | %s |" % (linha[0], linha[1], linha[2]))
            print("-" * 13)
        print("Jogador %s vence o Jogo %d!" % (jogadores[jogador_atual], numero_jogo))
        numero_jogo += 1
        jogador_atual = 0
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        continue

    cheio = True
    for linha in tabuleiro:
        if " " in linha:
            cheio = False
    if cheio:
        print("Estado final do Jogo %d:" % numero_jogo)
        for linha in tabuleiro:
            print("| %s | %s | %s |" % (linha[0], linha[1], linha[2]))
            print("-" * 13)
        print("O Jogo %d é um empate!" % numero_jogo)
        numero_jogo += 1  
        jogador_atual = 0  
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)] 
        continue

    jogador_atual = 1 - jogador_atual
