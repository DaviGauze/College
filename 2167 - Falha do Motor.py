N = int(input().strip())

rpm = list(map(int, input().strip().split()))

queda = 0
for i in range(1, N):
    if rpm[i] < rpm[i-1]:
        queda = i + 1
        break

print(queda)
