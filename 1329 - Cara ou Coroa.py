while True:
    N = int(input().strip())
    if N == 0:
        break
    
    resultados = list(map(int, input().strip().split()))
    
    vitorias_maria = 0
    vitorias_joao = 0
    
    for resultado in resultados:
        if resultado == 0:
            vitorias_maria += 1
        elif resultado == 1:
            vitorias_joao += 1
    
    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")
