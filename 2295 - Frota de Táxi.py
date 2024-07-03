entrada = input().strip()
A, G, Ra, Rg = map(float, entrada.split())

alcool = A / Ra
gasolina = G / Rg

if alcool < gasolina:
    print("A")
else:
    print("G")
