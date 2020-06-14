import random

nbmys = random.randint (1, 100)
essai_max = 5
print("Essayez de deviner un nombre entre 1 et 100.")

continuer = "o"
while continuer == "o":

    e = 0
    while e < essai_max : 
        nb = input("Essayez de deviner le nombre mystère? ")
        if not nb.isdigit() :
            print("Entrez uniquement des chiffres, s'il vous plaît! ")
            continue
       
        nb = int(nb)
        if nb < nbmys :
            print(f"Le nombre mystère est plus GRAND que {nb}. ")
        if nb > nbmys :
            print(f"Le nombre mystère est plus PETIT que {nb}. ")

        e += 1

        if nb == nbmys and e <= e + 5 :
            print(f"Felicitations, vous avez trouvé le nombre mystère en {e} essai(s) ! ")
            exit()
        elif nb != nbmys and e == essai_max :
            print(f"Dommage, vous avez épuisé vos {essai_max} essais! Le nombre mystère était {nbmys} ! ")
        
        
    continuer = input("Voulez-vous retenter votre chance avec un nouveau nombre mystère? o/n  ")     
    if not continuer == "o" :
        break
    nbmys = random.randint (1, 100)

   