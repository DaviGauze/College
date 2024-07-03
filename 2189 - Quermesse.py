teste = 1

while True:
    num = int(input())
    if num == 0:
        break
    
    ingressos = list(map(int, input().split()))
    
    ganhador = None
    for i in range(num):
        if ingressos[i] == i + 1:
            ganhador = ingressos[i]
            break
    
    print("Teste %d" % teste)
    print("%d" % ganhador)
    print("")
    
    teste += 1
