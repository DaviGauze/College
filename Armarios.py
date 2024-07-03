num_armarios = 10
armarios = ["Livre"] * num_armarios

while True:
    print("\nMENU")
    print("1 – Mostrar a situação de todos os armários")
    print("2 – Mostrar os armários livres")
    print("3 – Utilizar Armário")
    print("4 – Remover Armário")
    print("5 – Resumo dos Armários")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Situação de todos os armários:")
        for i in range(num_armarios):
            print(f"Armário {i}: {armarios[i]}")

    elif escolha == "2":
        livres = [i for i in range(num_armarios) if armarios[i] == "Livre"]
        if livres:
            print("Armários livres:", end=" ")
            for num in livres:
                print(f"Armário {num}", end=", ")
            print()
        else:
            print("Não há armários livres.")

    elif escolha == "3":
        num_armario = int(input("Informe o número do armário que deseja utilizar: "))
        if num_armario < 0 or num_armario >= num_armarios:
            print("Armário inválido.")
        elif armarios[num_armario] == "Ocupado":
            print("Armário sendo utilizado.")
        else:
            armarios[num_armario] = "Ocupado"
            print(f"Armário {num_armario} marcado como ocupado.")

    elif escolha == "4":
        num_armario = int(input("Informe o número do armário que deseja remover: "))
        if num_armario < 0 or num_armario >= num_armarios:
            print("Armário inválido.")
        elif armarios[num_armario] == "Livre":
            print("Armário não está sendo utilizado.")
        else:
            armarios[num_armario] = "Livre"
            print(f"Armário {num_armario} liberado.")

    elif escolha == "5":
        livres = sum(1 for estado in armarios if estado == "Livre")
        ocupados = sum(1 for estado in armarios if estado == "Ocupado")
        print(f"Resumo dos armários: {livres} Armários livres, {ocupados} Armários ocupados.")

    elif escolha == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
