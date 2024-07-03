print("Em qual evento você irá participar na semana esportiva?")
print("1) Campeonato de CS")
print("2) Vôlei Misto")
print("3) Truco")
print("4) Nenhuma das anteriores")
print("0) Sair")

votos = 0
CS = 0
Volei = 0
Truco = 0
Nenhuma = 0
Sair = 0

while True:
    opcao = int(input("Entre com sua opção: "))
    if opcao == 0:
        break
    votos += 1
    if opcao == 1:
        CS += 1
    elif opcao == 2:
        Volei += 1
    elif opcao == 3:
        Truco += 1
    elif opcao == 4:
        Nenhuma += 1

print(".........Estatísticas da pesquisa.........")
print("Total de votos foi de %d." % votos)
print("Total de votos no Campeonato de CS foi %d e teve %.2f%% de escolha." % (CS, CS/votos*100))
print("Total de votos no Vôlei Misto foi %d e teve %.2f%% de escolha." % (Volei, Volei/votos*100))
print("Total de votos no Truco foi %d e teve %.2f%% de escolha." % (Truco, Truco/votos*100))
print("Total de votos no Nenhuma foi %d e teve %.2f%% de escolha." % (Nenhuma, Nenhuma/votos*100))

if CS > Volei and CS > Truco and CS > Nenhuma:
    print("O pessoal prefere um CS")
elif Volei > CS and Volei > Truco and Volei > Nenhuma:
    print("O pessoal prefere Vôlei")
elif Truco > CS and Truco > Volei and Truco > Nenhuma:
    print("O pessoal prefere Truco")
elif Nenhuma > CS and Nenhuma > Volei and Nenhuma > Truco:
    print("O pessoal prefere outras coisas")
else:
    print("Empate")
    print("Qual é a sua opinião?")
    print("1) Campeonato de CS")
    print("2) Vôlei Misto")
    print("3) Truco")
    print("4) Nenhuma das anteriores")
    opiniao = int(input("Entre com sua opinião: "))
    if opiniao == 1:
        print("Você decidiu que o pessoal prefere um CS")
    elif opiniao == 2:
        print("Você decidiu que o pessoal prefere Vôlei")
    elif opiniao == 3:
        print("Você decidiu que o pessoal prefere Truco")
    elif opiniao == 4:
        print("Você decidiu que o pessoal prefere outras coisas")
