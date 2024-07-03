N = int(input())

total_s = total_b = total_a = 0
total_s1 = total_b1 = total_a1 = 0

for i in range(N):
    nome = input() 
    S, B, A = map(int, input().split())  
    S1, B1, A1 = map(int, input().split())

    total_s += S
    total_b += B
    total_a += A
    total_s1 += S1
    total_b1 += B1
    total_a1 += A1

percentual_saques = (total_s1 / total_s) * 100 if total_s > 0 else 0
percentual_bloqueios = (total_b1 / total_b) * 100 if total_b > 0 else 0
percentual_ataques = (total_a1 / total_a) * 100 if total_a > 0 else 0

print(f"Pontos de Saque: {percentual_saques:.2f} %.")
print(f"Pontos de Bloqueio: {percentual_bloqueios:.2f} %.")
print(f"Pontos de Ataque: {percentual_ataques:.2f} %.")