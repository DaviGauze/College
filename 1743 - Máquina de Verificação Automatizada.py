vet1 = []
vet2 = []
vet1 = list(map(int, input("").split()))
vet2 = list(map(int, input("").split()))
compativel = 0
for i in range(5):
    if vet1[i] != vet2[i]:
        compativel = compativel + 1
if compativel != 5:
    print("N")
else:
    print("Y")
