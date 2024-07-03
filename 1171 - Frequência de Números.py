N = int(input())

frequencia = {}

for i in range(N):
    numero = int(input())
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

numeros_ordenados = sorted(frequencia.keys())

for numero in numeros_ordenados:
    print(f"{numero} aparece {frequencia[numero]} vez(es)")
