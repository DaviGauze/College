def identificar_animal(categoria1, categoria2, categoria3):
    if categoria1 == 'vertebrado':
        if categoria2 == 'ave':
            if categoria3 == 'carnivoro':
                return 'aguia'
            elif categoria3 == 'onivoro':
                return 'pomba'
        elif categoria2 == 'mamifero':
            if categoria3 == 'onivoro':
                return 'homem'
            elif categoria3 == 'herbivoro':
                return 'vaca'
    elif categoria1 == 'invertebrado':
        if categoria2 == 'inseto':
            if categoria3 == 'hematofago':
                return 'pulga'
            elif categoria3 == 'herbivoro':
                return 'lagarta'
        elif categoria2 == 'anelideo':
            if categoria3 == 'hematofago':
                return 'sanguessuga'
            elif categoria3 == 'onivoro':
                return 'minhoca'
    return 'Animal desconhecido'

categoria1 = input().strip()
categoria2 = input().strip()
categoria3 = input().strip()

animal = identificar_animal(categoria1, categoria2, categoria3)

print(animal)
